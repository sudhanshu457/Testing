import os
import ssl
import pika
import sys
from datetime import datetime
import logging
import time
# logging.basicConfig(filename="/usr/src/app/logs/producer.log", 
#                     format='%(asctime)s %(message)s') 

logger=logging.getLogger()
logger.setLevel(logging.DEBUG)
username='guest'
password='guest'
hostname=os.environ.get('hostname')
cacert=os.environ.get('cacert')
producercert=os.environ.get('producercert')
producerkey=os.environ.get('producerkey')
credentials = pika.PlainCredentials(username, password)
tmp='na'
if str(cacert)==str(tmp):
    print("in if ")
    parameters = pika.ConnectionParameters(hostname,
                                        5672,
                                        '/',
                                        credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
else:
    context = ssl.create_default_context(
                                cafile= cacert
                                )
    context.load_cert_chain(producercert,producerkey)
    ssl_options = pika.SSLOptions(context, "rabbitmq")
    parameters = pika.ConnectionParameters(port=5671,
                                            host=hostname,
                                            connection_attempts=5,
                                            retry_delay=5,
                                            ssl_options=ssl_options)
    connection = pika.BlockingConnection(parameters)
    logger.info("connection established woth rabbitmq at port 5671 sucessfully")
    channel = connection.channel()
    
        
def main():
    channel.queue_declare(queue='hello', durable=True)
    i=5
    while i>=0:
        #channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
        channel.basic_publish(exchange='', routing_key='hello', body='Hello World!', properties=pika.BasicProperties(delivery_mode = 2,))
        print("sent hello world message !")
        i=i-1
    while True:
        pass
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
