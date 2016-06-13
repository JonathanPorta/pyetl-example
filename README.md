# pyetl-example
This is meant to be a 'good' example of how to use the pyetl-framework.

## Setting up Local Development
First, you'll need to setup a few things in your local environment. Be sure you have python 3.5 and autoenv installed. Then, clone this repo and cd into it. A Makefile is provided and should be enough to get you started. Start by using autoenv to setup your env. You can use the convenience function below if you'd prefer:

`make setup_local_dev`

From there, you'll need to be sure the env has been sourced by running:

`source env/bin/activate`

Now we can begin installing the app's dependencies:

`make install_deps`

As long as the dependencies were installed successfully, we can continue onto setting up a local Redis flop-house, err instance, for your queue. In order for this to work, you will need to have Docker installed. We use the default official Redis container with no customization or security for local development. A helper to set this up for you is also provided in the Makefile:

`make setup_local_redis`

### Help, it's broke!
If you get into trouble with any of the above, you make want to start over. But, first, run `make clean` to remove any borked dependency installations or errant Redis containers. The make commands are not idompotent so you need to cleanup before re-running commands.

## Deploying on Heroku
So, it looks like you want to deploy this on Heroku for some reason. Again, our makefile contains a task for logging you into Heroku, creating a new Heroku project, and then adding Heroku remotes to your local checkout of this repository. If you don't want to deploy this using git pushes to Heroku's servers, then this section will be of little help to you. Stop reading now.

### Stuff You Need Before you Begin
You will need a Heroku account with a valid payment instrument because currently it appears that the only way Heroku will let you spinup Redis for a project is if you have a payment method on file. You will also need to install the Heroku CLI.

With the Heroku CLI installed and your Heroku account setup, you can just run the following command and everything will be setup for you:

`make setup_heroku`

You may want/need to change the value of `APP_NAME` on the first line of the Makefile.

Once setup, deploying on Heroku is as easy as:

`make deploy_staging`
`make deploy_production`

By default, both `deploy_*` assume that the code you want deployed is committed to the `master` branch. When deploying to Heroku via git pushes, obviously the code you want deployed must be committed. But, if you'd like to push a branch other than `master` to staging or production then you can do so manually:

`git push heroku-staging the_name_of_my_branch`
