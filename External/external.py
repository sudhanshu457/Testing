import os
import ssl
import pika
import sys
from datetime import datetime
import logging
import time
# logging.basicConfig(filename="/usr/src/app/logs/external.log", 
#                     format='%(asctime)s %(message)s') 

logger=logging.getLogger()
logger.setLevel(logging.DEBUG)
username='guest'
password='guest'
hostname=os.environ.get('hostname')
cacert=os.environ.get('cacert')
externalcert=os.environ.get('externalcert')
externalkey=os.environ.get('externalkey')
credentials = pika.PlainCredentials(username, password)
tmp='na'

print("making connection without certificates..non-ssl connection")
parameters = pika.ConnectionParameters(hostname,
                                    5672,
                                    '/',
                                    credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
       
def main():
    channel.queue_declare(queue='hello')
    i=5
    while i>=0:
        channel.basic_publish(exchange='', routing_key='hello', body='Hello World external!')
        print("sent hello world message through external !")
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