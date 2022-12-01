FROM python:3.10-buster

RUN mkdir /tcw_tasks
WORKDIR /tcw_tasks

COPY ./requirements.txt /tcw_tasks
RUN pip install -r requirements.txt
RUN pip install -e .

RUN apt-get update && apt-get install -y cron
COPY cron.txt /etc/cron.d/tcw-crontab
RUN chmod 0644 /etc/cron.d/tcw-crontab &&
    crontab /etc/cron.d/tcw-crontab
