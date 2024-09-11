FROM python:3.12

RUN mkdir /app

WORKDIR /app

COPY req.txt .

RUN pip install -r req.txt

COPY . .

WORKDIR src

CMD gunicorn main:app --bind=0.0.0.0:8080