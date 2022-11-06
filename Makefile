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
		uvicorn backend:app --reload

backend-docker-build:
	docker build -f backend/Dockerfile -t camerge-backend .

backend-docker-run: backend-docker-build
	docker run --rm -p 8000:8000 camerge-backend


# cloud function stuff
cloud-function-deployment:
	# first we clean up and create new base
	rm -rf cloud_function_deployment || true;
	mkdir cloud_function_deployment;
	# create merged requirements.txt
	cat cloud_function/requirements.txt >> cloud_function_deployment/requirements.txt;
	cat common/requirements.txt >> cloud_function_deployment/requirements.txt;
	# copy all relevant code and clean what is not needed
	cp -r common cloud_function_deployment/common && \
		rm cloud_function_deployment/common/*.md && \
		rm cloud_function_deployment/common/*.txt;
	cp -r cloud_function cloud_function_deployment/cloud_function && \
		rm cloud_function_deployment/cloud_function/*.md && \
		rm cloud_function_deployment/cloud_function/*.txt;
	# now move main.py to correct location
	mv cloud_function_deployment/cloud_function/main.py cloud_function_deployment/main.py;

cloud-function-run:
	# first prepare build
	$(MAKE) cloud-function-deployment;
	# and now run it
	source venv/bin/activate && \
		cd cloud_function_deployment && \
		functions-framework --target app --debug --port=8000;