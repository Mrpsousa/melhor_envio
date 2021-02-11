FROM alpine:3.12.3
RUN apk --update add python3 libjpeg py3-pip postgresql-dev --no-cache
RUN apk add --no-cache --virtual dependencias gcc make musl-dev openssl-dev libffi-dev zlib-dev python3-dev jpeg-dev
RUN mkdir /code
COPY . /code/
RUN pip install --no-cache-dir -r /code/requirements.txt
RUN apk del dependencias
WORKDIR /code

CMD python3 manage.py runserver 0.0.0.0:8000
