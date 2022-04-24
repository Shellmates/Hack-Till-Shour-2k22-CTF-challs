FROM frolvlad/alpine-glibc:glibc-2.34

RUN apk update && apk add socat

COPY challenge /challenge

WORKDIR /challenge

RUN chmod +x entrypoint.sh challenge && \
    chown -R root:root .
    
EXPOSE 1337

ENTRYPOINT ["/challenge/entrypoint.sh"]