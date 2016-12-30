## README ##

This Node based REST app is part of a collection of software for a personal side project, inspired by [Jane Kim](http://janekim.me/)'s own project by the same name, aimed at tracking different aspects of my personal life.

life-api-server is a collection of APIs that represent data pertaning to my personal life, designed to be consumed by client facing applications part of this software collection.

### GETTING STARTED ###

1. Clone repo.
2. Install [Node](https://nodejs.org/en/) and [MongoDB](https://www.mongodb.com/).
3. Run `npm install`
4. Create local database paths `/data/mongodb/life-api` and `/data/mongodb/backups`
5. Start local database by running `npm run db-start`.
6. Build application by running `npm run build`.
7. Start server by running `npm start`.
8. All set!

### DEPLOY ###
To use the `deploy.py` script, follow the steps below:

1. Ensure you have a Python environment set up on your machine.
2. Run `pip install virtualenv`.
3. Create your virtualenv by running `virtualenv life-api-server` (this path has been added to `.gitignore`).
4. Activate virtualenv by running `source life-api-server/bin/activate`.
5. Install frozen dependencies by running `pip install -r requirements.txt`.
6. Modify `settings.py` fields to match your environment.

You should now be able to run the deploy script via `fab deploy`. Follow prompts to deploy code.
