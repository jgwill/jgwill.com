FROM jgwill/node:16.14.0

#RUN apt update && apt upgrade -y

RUN npm install  @angular/cli --g

RUN useradd -rm -d /home/jgi -s /bin/bash -g root -G sudo -u 1000 jgi
USER jgi

WORKDIR /app
