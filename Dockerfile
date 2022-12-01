FROM python:3.10-buster

# compile and install driver for postgresql
RUN apt-get update && apt-get install -y libpq-dev gcc
RUN pip install psycopg2

# install the tcwinners script from pypi
RUN pip install tcw-tasks

# install cron services, and put cronjob in place
RUN apt-get update && apt-get install -y cron
COPY cron.txt /etc/cron.d/tcw-crontab
RUN chmod 0644 /etc/cron.d/tcw-crontab &&
    crontab /etc/cron.d/tcw-crontab
