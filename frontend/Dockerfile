# Stage 1: Build React app
FROM node:14 as build

WORKDIR /app
COPY . /app

RUN npm install
RUN npm run build

# Stage 2: Serve React app using NGINX
FROM nginx:alpine

COPY --from=build /app/build /usr/share/nginx/html

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]

