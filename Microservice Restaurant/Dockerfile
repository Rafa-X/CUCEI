FROM node:alpine

WORKDIR /src

ADD package.json ./

RUN npm install
#daemon process manager for online applications
RUN npm i -g pm2  
RUN npm install -g nodemon
#MODULES FOR THE SERVICES
RUN npm install axios
RUN npm install cote
RUN npm install body-parser
RUN npm install express --save

ADD . .