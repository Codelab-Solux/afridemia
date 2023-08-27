# syntax=docker/dockerfile:1
FROM python:3.11-alpine
ADD requirements.txt /app/requirements.txt
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
ADD dashboard /app/dashboard
ADD schools /app/schools
ADD static /app/static
ADD templates /app/templates
ADD media /app/media
ADD manage.py /app/manage.py
WORKDIR /app

ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "afridemia.wsgi:application"]