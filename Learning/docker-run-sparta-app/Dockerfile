# FROM which image
FROM node:20-slim

# set working dir to "app" folder in container
WORKDIR /app

# copy package.json package-lock.json only
COPY app/package.json app/package-lock.json ./

# run npm ci for production
RUN npm ci --omit=dev

# set working dir to "app" folder in container
# FROM which image
FROM node:20-slim

# set working dir to "app" folder in container
WORKDIR /app

# copy package.json package-lock.json only
COPY app/package.json app/package-lock.json ./

# run npm ci for production ignores running 
RUN npm ci --omit=dev --ignore-scripts

# set working dir to "app" folder in container
WORKDIR /app

# COPY . .
COPY app/ .

# use "node" user
USER node

# expose app on port 3000
EXPOSE 3000

# run the node app using index.js
CMD ["node", "index.js"]
