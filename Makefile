# common
APP_PORT := 8080

# pipenv
create-venv: ./venv
	python -m venv ./venv

install-deps: create-venv
	source venv/bin/activate && \
		pip install -r backend/requirements.txt && \
		pip install -r common/requirements.txt && \
		pip install -r cloud_function/requirements.txt

# backend stuff
backend-run:
	source venv/bin/activate && \
		uvicorn backend:app --reload --port $(APP_PORT)

backend-docker-build:
	docker build -f backend/Dockerfile -t camerge-backend .

backend-docker-run: backend-docker-build
	docker run --rm -p $(APP_PORT):8080 camerge-backend


# cloud function stuff
CLOUD_FUNCTION_OUTPUT_FOLDER := cloud_function_deployment
CLOUD_FUNCTION_ZIP := camerge_service_cloud_function.zip

cloud-function-prepare:
	# first we clean up and create new base
	rm -rf $(CLOUD_FUNCTION_OUTPUT_FOLDER) || true;
	mkdir $(CLOUD_FUNCTION_OUTPUT_FOLDER);
	# create merged requirements.txt
	cat cloud_function/requirements.txt >> $(CLOUD_FUNCTION_OUTPUT_FOLDER)/requirements.txt;
	echo '\n' >> $(CLOUD_FUNCTION_OUTPUT_FOLDER)/requirements.txt;
	cat common/requirements.txt >> $(CLOUD_FUNCTION_OUTPUT_FOLDER)/requirements.txt;
	# copy all relevant code and clean what is not needed
	cp -r common $(CLOUD_FUNCTION_OUTPUT_FOLDER)/common && \
		rm $(CLOUD_FUNCTION_OUTPUT_FOLDER)/common/*.md && \
		rm $(CLOUD_FUNCTION_OUTPUT_FOLDER)/common/*.txt;
	cp -r cloud_function $(CLOUD_FUNCTION_OUTPUT_FOLDER)/cloud_function && \
		rm $(CLOUD_FUNCTION_OUTPUT_FOLDER)/cloud_function/*.md && \
		rm $(CLOUD_FUNCTION_OUTPUT_FOLDER)/cloud_function/*.txt;
	# now move main.py to correct location
	mv $(CLOUD_FUNCTION_OUTPUT_FOLDER)/cloud_function/main.py $(CLOUD_FUNCTION_OUTPUT_FOLDER)/main.py;

cloud-function-deployment:
	$(MAKE) cloud-function-prepare;
	cd $(CLOUD_FUNCTION_OUTPUT_FOLDER) && \
 		zip -r ../$(CLOUD_FUNCTION_ZIP) *;
	rm -rf $(CLOUD_FUNCTION_OUTPUT_FOLDER);

cloud-function-clean:
	rm -rf $(CLOUD_FUNCTION_OUTPUT_FOLDER) || true;
	rm -rf $(CLOUD_FUNCTION_ZIP) || true;

cloud-function-run:
	# first prepare build
	$(MAKE) cloud-function-prepare;
	# and now run it
	source venv/bin/activate && \
		cd $(CLOUD_FUNCTION_OUTPUT_FOLDER) && \
		functions-framework --target app --debug --port=$(APP_PORT);