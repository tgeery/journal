FROM python:3
COPY . /tmp/blog
WORKDIR /tmp/blog
RUN pip3 install django psycopg2 dj_static
