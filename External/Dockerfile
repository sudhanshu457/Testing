FROM python:2.7-alpine
RUN pip install pika
RUN pip install --upgrade pip enum34
ENV PYTHONUNBUFFERED=1

RUN mkdir /certificate
WORKDIR /certificate
RUN mkdir /external
RUN mkdir /CA
WORKDIR /usr/src/app
RUN mkdir /logs
COPY external.py .
CMD ["python", "/usr/src/app/external.py"]
