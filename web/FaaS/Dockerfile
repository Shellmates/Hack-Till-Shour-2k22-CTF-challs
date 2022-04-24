FROM php:7.3-apache

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get -y --no-install-recommends install figlet

COPY challenge /var/www/html

COPY flag.txt /

WORKDIR /var/www/html

RUN chown root:root /var/www/html
