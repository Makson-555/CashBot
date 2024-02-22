FROM python:3

ENV PYTHONUNBUFFERED 1

RUN mkdir /CashBot

WORKDIR /CashBot

COPY web/requirements.txt /CashBot/

RUN pip install --upgrade pip && pip install -r requirements.txt

RUN apt-get update && apt-get install -y cron

ADD . /CashBot/

CMD ["cron", "-f"]
