FROM node:16

WORKDIR /front
ENV PATH /front/node_modules/.bin:$PATH

COPY package.json ./
RUN yarn install

COPY . ./

CMD ["npm", "start"]
