FROM rabbitmq:3.6-management-alpine
COPY rabbitmq.config ./etc/rabbitmq/rabbitmq.config
RUN mkdir /certificate
WORKDIR /certificate
RUN mkdir /rabbitmq
RUN mkdir /CA

CMD rabbitmq-server
	
# CMD tail -f /dev/null