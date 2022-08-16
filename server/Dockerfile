FROM python:3.9-slim

WORKDIR /usr/src/server
RUN pip install --upgrade pip


RUN pip install psycopg2-binary requests

COPY . /usr/src/server
RUN chmod 777 /usr/src/server

CMD [ "python", "main.py" ]


