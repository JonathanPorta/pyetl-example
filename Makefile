APP_NAME := pyetl-example

install_deps:
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

deploy_staging:
	git push heroku-staging master

deploy_production:
	git push heroku-production master