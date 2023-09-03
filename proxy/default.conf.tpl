# configuration of the server
server {
        listen ${LISTEN_PORT};
        server_name afridemia.com www.afridemia.com;
        charset utf-8;

        # Django media and static files
        location /media  {
                alias /media/;
        }
        location /static {
                alias /static/;
        }
        # uwsgi setup
        location / {
                uwsgi_pass ${APP_HOST}:${APP_PORT};
                include /etc/nginx/uwsgi_params;
                client_max_body_size 75M;
        }

}