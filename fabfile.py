#!/usr/bin/env python

import sys
import json

from fabric.api import env, task, cd, run, prompt

from settings import REMOTE_HOST, REMOTE_CODE_DIR, PM2_APP_NAME

# CONFIG
env.hosts = [REMOTE_HOST]
env.use_ssh_config = True


def get_version():
    with open('package.json') as package_file:
        package = json.load(package_file)

    return package['version']


@task
def deploy():
    print 'Running on {0} as {1}'.format(env.hosts, env.user)

    default_tag = get_version()

    tag = prompt('Please enter {0} {1} [default: {2}]: '.format('tag', '(eg. 1.0.0)', default_tag))
    tag = default_tag if tag in [None, ''] else tag

    with cd(REMOTE_CODE_DIR):
        run('git checkout master')
        run('git pull')
        run('git checkout tags/{0}'.format(tag))
        run('npm run build')
        run('npm prune')
        run('npm install')
        run('sudo pm2 reload {0}'.format(PM2_APP_NAME))

    print 'Successfully deployed {0} version {1}'.format(PM2_APP_NAME, default_tag)


@task
def pm2_start():
    print 'Running on {0} as {1}'.format(env.hosts, env.user)

    run('sudo pm2 start {0}/app/dist/index.js --name {1}'.format(REMOTE_CODE_DIR, PM2_APP_NAME))

    print 'Successfully spawned {0}'.format(PM2_APP_NAME)


@task
def pm2_stop():
    print 'Running on {0} as {1}'.format(env.hosts, env.user)

    run('sudo pm2 stop {0}'.format(PM2_APP_NAME))

    print 'Successfully stopped {0}'.format(PM2_APP_NAME)


@task
def pm2_restart():
    print 'Running on {0} as {1}'.format(env.hosts, env.user)

    run('sudo pm2 restart {0}'.format(PM2_APP_NAME))

    print 'Successfully resumed {0}'.format(PM2_APP_NAME)


@task
def pm2_delete():
    print 'Running on {0} as {1}'.format(env.hosts, env.user)

    run('sudo pm2 delete {0}'.format(PM2_APP_NAME))

    print 'Successfully deleted {0}'.format(PM2_APP_NAME)
