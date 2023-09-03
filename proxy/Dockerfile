FROM nginx:1.24.0-alpine

LABEL maintainer='afridemia.com'

COPY ./default.conf.tpl /etc/nginx/default.conf.tpl

COPY ./uwsgi_params /etc/nginx/uwsgi_params

COPY ./run.sh /run.sh

ENV LISTEN_PORT = 8080
ENV APP_HOST = app
ENV APP_PORT = 8000

CMD ["/run.sh"]