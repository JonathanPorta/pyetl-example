APP_NAME := pyetl-example
# set a default for the port if none is specified
ifeq ($(PORT),)
	PORT := 5000
endif

install: python_deps

python_deps:
	pip install -r requirements.txt

clean_deps:
	rm -rf env

setup_local_dev:
	pyvenv-3.4 env
	@echo 'Please activate the environment by running: `source env/bin/activate` or by using something like autoenv to autoload the localized env when you enter the directory.'

setup_local_redis:
	@echo "Spinning up a Redis container with tag '$(APP_NAME)-redis'..."
	$(eval DOCKER_REDIS_CONTAINER = $(shell docker run -p 127.0.0.1:6379:6379 --name $(APP_NAME)-redis -d redis))

	@echo 'Redis listening on: '
	docker port $(DOCKER_REDIS_CONTAINER)

clean_redis:
	@echo "Cleaning up any Redis containers with tag '$(APP_NAME)-redis'..."
	-docker rm -f $(APP_NAME)-redis

clean: clean_deps clean_redis

setup_heroku:
	heroku auth:whoami ; if [ $$? -neq 0 ] ; then heroku login ; fi
	heroku create $(APP_NAME)-staging
	heroku create $(APP_NAME)-production
	git remote add heroku-staging git@heroku.com:$(APP_NAME)-staging.git
	git remote add heroku-production git@heroku.com:$(APP_NAME)-production.git

setup_heroku_env:
	heroku config:set APP_SETTINGS=StagingConfig --remote heroku-staging
	heroku config:set APP_SETTINGS=ProductionConfig --remote heroku-production

setup_heroku_secrets:
	# s3 credentials
	heroku config:set S3_ACCESS_ID=${S3_ACCESS_ID} --remote heroku-staging
	heroku config:set S3_SECRET_KEY=${S3_SECRET_KEY} --remote heroku-staging

	# http proxy creds
	heroku config:set PROXY_HTTP_HOSTNAME=${PROXY_HTTP_HOSTNAME} --remote heroku-staging
	heroku config:set PROXY_HTTP_USERNAME=${PROXY_HTTP_USERNAME} --remote heroku-staging
	heroku config:set PROXY_HTTP_PASSWORD=${PROXY_HTTP_PASSWORD} --remote heroku-staging
	heroku config:set PROXY_HTTP_PORT=${PROXY_HTTP_PORT} --remote heroku-staging

	# https proxy creds
	heroku config:set PROXY_HTTPS_HOSTNAME=${PROXY_HTTPS_HOSTNAME} --remote heroku-staging
	heroku config:set PROXY_HTTPS_USERNAME=${PROXY_HTTPS_USERNAME} --remote heroku-staging
	heroku config:set PROXY_HTTPS_PASSWORD=${PROXY_HTTPS_PASSWORD} --remote heroku-staging
	heroku config:set PROXY_HTTPS_PORT=${PROXY_HTTPS_PORT} --remote heroku-staging

	# s3 credentials
	heroku config:set S3_ACCESS_ID=${S3_ACCESS_ID} --remote heroku-production
	heroku config:set S3_SECRET_KEY=${S3_SECRET_KEY} --remote heroku-production

	# http proxy creds
	heroku config:set PROXY_HTTP_HOSTNAME=${PROXY_HTTP_HOSTNAME} --remote heroku-production
	heroku config:set PROXY_HTTP_USERNAME=${PROXY_HTTP_USERNAME} --remote heroku-production
	heroku config:set PROXY_HTTP_PASSWORD=${PROXY_HTTP_PASSWORD} --remote heroku-production
	heroku config:set PROXY_HTTP_PORT=${PROXY_HTTP_PORT} --remote heroku-production

	# https proxy creds
	heroku config:set PROXY_HTTPS_HOSTNAME=${PROXY_HTTPS_HOSTNAME} --remote heroku-production
	heroku config:set PROXY_HTTPS_USERNAME=${PROXY_HTTPS_USERNAME} --remote heroku-production
	heroku config:set PROXY_HTTPS_PASSWORD=${PROXY_HTTPS_PASSWORD} --remote heroku-production
	heroku config:set PROXY_HTTPS_PORT=${PROXY_HTTPS_PORT} --remote heroku-production

setup_heroku_redis:
	heroku addons:create redistogo:nano --app $(APP_NAME)-staging
	heroku addons:create redistogo:nano --app $(APP_NAME)-production

deploy_staging:
	git push heroku-staging master

deploy_production:
	git push heroku-production master

run_flask:
	APP_BASEDIR=$(shell pwd) FLASK_PORT=${PORT} FLASK_HOSTNAME='0.0.0.0' pyetl_flask # pip should link this as an executable when the pyetl dependency is installed.

run_worker:
	APP_BASEDIR=$(shell pwd) pyetl_worker # pip should link this as an executable when the pyetl dependency is installed.
