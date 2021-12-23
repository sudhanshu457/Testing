
FROM alpine

RUN apk update && apk add --no-cache openssl && rm -rf /var/cache/apk/*
RUN apk add --update
RUN apk add --no-cache python3 && python3 -m ensurepip && pip3 install --upgrade pip setuptools 
RUN export PATH="/usr/bin/python3:$PATH"
RUN export PATH="/usr/bin/openssl:$PATH"
RUN pip install  Flask>=1.0.0
RUN pip install  flask-oidc>=1.4.0
RUN mkdir /app
WORKDIR /app
RUN mkdir /new_certs
ADD . /app/
RUN mkdir /logs
EXPOSE 5000
CMD ["python3", "/app/script.py"]
