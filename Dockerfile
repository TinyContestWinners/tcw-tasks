FROM python:3.10-buster

RUN apt-get update && apt-get install -y libpq-dev gcc
RUN pip install psycopg2

RUN pip install tcw-tasks

RUN apt-get update && apt-get install -y cron
COPY cron.txt /etc/cron.d/tcw-crontab
RUN chmod 0644 /etc/cron.d/tcw-crontab && crontab /etc/cron.d/tcw-crontab
