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