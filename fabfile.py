#!/usr/bin/env python

import sys
import json

from fabric.api import env, task, cd, run, prompt

from settings import HOST, CODE_DIR, PM2_APP_NAME

# CONFIG
env.hosts = [HOST]
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

    with cd(CODE_DIR):
        run('git checkout master')
        run('git pull')
        run('git checkout tags/{0}'.format(tag))
        run('npm run build')
        run('npm prune')
        run('npm install')
        run('sudo pm2 reload {0}'.format(PM2_APP_NAME))
