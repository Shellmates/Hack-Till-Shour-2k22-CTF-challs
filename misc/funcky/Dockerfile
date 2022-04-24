FROM python:3.10

RUN apt-get update && \
    apt-get install -y socat 

COPY ./challenge /challenge

RUN chmod 500 /challenge/entrypoint.sh

RUN chmod 511 /challenge/script.py

EXPOSE 1337

ENTRYPOINT ["/challenge/entrypoint.sh"]
