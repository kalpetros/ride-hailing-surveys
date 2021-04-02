FROM node:15-stretch

WORKDIR /srv
EXPOSE 1234

# Let Docker cache dependencies
COPY ./package.json ./
RUN yarn install

COPY . /srv

CMD ["yarn", "develop"]
