FROM python:latest

WORKDIR /app

COPY req.txt req.txt

RUN pip install --no-cache-dir --upgrade -r req.txt

COPY . .

CMD gunicorn main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8080