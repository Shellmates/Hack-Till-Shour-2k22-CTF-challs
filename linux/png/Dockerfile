FROM ubuntu:20.04


RUN apt-get update && \
    apt-get install -y socat

RUN useradd -m -d /home/png -s /bin/bash png

COPY challenge/flag.png /home/png

RUN find /home/png -exec chown root:root {} \; && \ 
    find /home/png -type f -exec chmod 774 {} \; && \
    find /home/png -type d -exec chmod 775 {} \;

RUN chmod o=wxt /tmp 

EXPOSE 1337

ENTRYPOINT /entrypoint.sh
COPY challenge/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

WORKDIR /home/png

USER png

