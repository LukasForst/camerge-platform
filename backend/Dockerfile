# needs to be run with root context (../ from this folder)
FROM python:3.11.0-slim

WORKDIR /app

# copy requirements
COPY backend/requirements.txt ./backend/requirements.txt
COPY common/requirements.txt ./common/requirements.txt

# install requirements
RUN pip install -r ./backend/requirements.txt && \
    pip install -r ./common/requirements.txt

# now copy code
COPY backend ./backend/
COPY common ./common/

# settings
EXPOSE 8000
# and start it up
CMD ["uvicorn", "backend:app", "--host", "0.0.0.0", "--port", "8000"]
