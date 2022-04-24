FROM python:2.7-slim

RUN apt update && apt install -y socat

COPY challenge /challenge

WORKDIR /challenge

RUN chmod +x entrypoint.sh entry.sh script.py

EXPOSE 1337

ENTRYPOINT ["/challenge/entrypoint.sh"]


