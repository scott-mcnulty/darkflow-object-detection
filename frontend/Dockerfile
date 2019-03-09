FROM node:10-alpine

# Add code
COPY src /app/src
COPY package.json angular.json package-lock.json tsconfig.json tslint.json /app/
WORKDIR /app/

# Install dependecies
RUN npm install

EXPOSE 4200

CMD [ "npm", "start" ]