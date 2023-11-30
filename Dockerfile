FROM python:3.11-slim

WORKDIR /app
COPY ./server /app

COPY requirements.txt requirements.txt 

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=api.py
ENV FLASK_RUN_HOST=0.0.0.0

CMD ["flask", "run"]
