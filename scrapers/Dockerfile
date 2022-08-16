FROM python:3.9-slim

WORKDIR /usr/src/scrapers
RUN pip install --upgrade pip

COPY ./requirements.txt /usr/src/scrapers/requirements.txt
RUN pip install -r requirements.txt

COPY . /usr/src/scrapers
RUN chmod 777 /usr/src/scrapers

CMD [ "scrapy", "crawl", "reality" ]


