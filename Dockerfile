FROM nginx:alpine

Copy maintenance /usr/share/nginx/html/maintenance

Copy default.conf /etc/nginx/conf.d/default.conf