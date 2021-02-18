FROM alpine:3.12.3
RUN apk --update add python3 py3-pip postgresql-dev --no-cache
RUN mkdir /code
COPY . /code/
RUN pip install --no-cache-dir -r /code/requirements.txt
RUN apk del dependencias
WORKDIR /code

CMD python3 manage.py runserver
