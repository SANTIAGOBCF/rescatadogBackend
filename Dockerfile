# Dockerfile

FROM python:3.10.4-buster

# install nginx
RUN apt-get update && apt-get install nginx vim -y --no-install-recommends
COPY nginx.default /etc/nginx/sites-available/default
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

# copy source and install dependencies
RUN mkdir -p /opt/app
RUN mkdir -p /opt/app/rescatadog
COPY . /opt/app/rescatadog/
COPY requirements.txt start-server.sh /opt/app/rescatadog
WORKDIR /opt/app/rescatadog
RUN pip install -r requirements.txt
RUN chown -R www-data:www-data /opt/app/rescatadog

# start server
EXPOSE 8020
STOPSIGNAL SIGTERM
CMD ["/opt/app/rescatadog/start-server.sh"]
