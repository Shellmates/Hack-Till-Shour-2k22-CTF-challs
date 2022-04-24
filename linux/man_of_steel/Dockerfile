FROM ubuntu:18.04

RUN apt-get update &&\
    apt-get install -y openssh-server &&\
    apt install -y man-db

RUN useradd -M -s /bin/bash ctf

RUN echo 'ctf:ctf' | chpasswd

RUN touch flag

RUN echo "Get some help!!" >flag

RUN mkdir /usr/local/man/man1 /usr/local/man/man4

COPY ./flag.1.gz /usr/local/man/man1/flag.1.gz

COPY ./flag.4.gz /usr/local/man/man4/flag.4.gz

ENTRYPOINT service ssh start && tail -f /dev/null
