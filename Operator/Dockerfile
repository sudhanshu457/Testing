FROM python:3.7
RUN mkdir /src
WORKDIR /src
RUN mkdir /logs
ADD myoperator.py /src

RUN pip install kopf
RUN pip install kubernetes
COPY . /src
CMD kopf run /src/myoperator.py --verbose