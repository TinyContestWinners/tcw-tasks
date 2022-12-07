FROM python:3.10-buster

RUN apt-get update && apt-get install -y libpq-dev gcc
RUN pip install psycopg2
RUN pip install tcw-tasks
