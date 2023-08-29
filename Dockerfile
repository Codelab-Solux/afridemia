FROM python:3.11-alpine

# COPY ./requirements.txt /app

ADD requirements.txt /app/requirements.txt
# COPY afridemia /app


RUN set -ex \
    && apk add --no-cache --virtual .build-deps postgresql-dev build-base \
    && python -m venv /env \
    && /env/bin/pip install --upgrade pip \
    && /env/bin/pip install --no-cache-dir -r /app/requirements.txt \
    && runDeps="$(scanelf --needed --nobanner --recursive /env \
    | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
    | sort -u \
    | xargs -r apk info --installed \
    | sort -u)" \
    && apk add --virtual rundeps $runDeps \
    && apk del .build-deps

ADD accounts /app/accounts
ADD afridemia /app/afridemia
ADD base /app/base
ADD compose.yaml /app/compose.yaml
ADD dashboard /app/dashboard
ADD Dockerfile /app/Dockerfile
ADD env /app/env
ADD manage.py /app/manage.py
ADD nginx /app/nginx
ADD schools /app/schools
ADD static /app/static
ADD templates /app/templates
RUN mkdir -p /app/media

WORKDIR /app

COPY ./entrypoint.sh /
# ENV VIRTUAL_ENV ./env
# ENV PATH ./env/bin:$PATH

# EXPOSE 8000

# CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "afridemia.wsgi:application"]
ENTRYPOINT [ "sh", "/entrypoint.sh" ]