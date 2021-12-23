FROM python:2.7-alpine
RUN pip install pika
RUN pip install --upgrade pip enum34
ENV PYTHONUNBUFFERED=1

RUN mkdir /certificate
WORKDIR /certificate
RUN mkdir /producer
RUN mkdir /CA
WORKDIR /usr/src/app
RUN mkdir /logs
COPY producer.py .

CMD ["python", "/usr/src/app/producer.py"]
