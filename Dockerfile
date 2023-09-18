FROM python:3.11-alpine

LABEL maintainer="afridemia.com"

ENV PYTHONUNBUFFERED 1

COPY . /app

WORKDIR /app

EXPOSE 8000

RUN python -m venv /env && \
    /env/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-deps \
    build-base postgresql-dev musl-dev && \
    /env/bin/pip install -r /app/requirements.txt && \
    apk del .tmp-deps && \
    adduser --disabled-password --no-create-home afridemia_app && \
    mkdir -p /app/media

ENV PATH="/env/bin:$PATH"

USER afridemia_app

CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "afridemia.wsgi:application"]
# ENTRYPOINT [ "sh", "/entrypoint.sh" ]