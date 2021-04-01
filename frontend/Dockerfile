FROM node:12-alpine

WORKDIR /srv
EXPOSE 1234

# Let Docker cache dependencies
COPY ./package.json ./
COPY ./yarn.lock ./
RUN yarn install

COPY . /srv

CMD ["yarn", "develop"]
