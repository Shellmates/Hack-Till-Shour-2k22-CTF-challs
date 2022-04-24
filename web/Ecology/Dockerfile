FROM node:alpine3.15

COPY app /app

WORKDIR /app

RUN npm install

ENTRYPOINT ["npm", "run", "start"]