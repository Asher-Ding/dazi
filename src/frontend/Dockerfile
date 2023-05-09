# Dockerfile.dev
# docker build -t vue-dev -f Dockerfile.dev .
# docker run -it --rm -v $(pwd)/:/app -p 8080:8080 vue-dev

FROM node:14

WORKDIR /frontend

COPY package.json ./
RUN npm install

COPY . .

CMD ["npm","run","dev:mp-weixin"]