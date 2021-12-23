import pika, sys, os, ssl
import logging
import time
# logging.basicConfig(filename="cp.log", 
#                     format='%(asctime)s %(message)s') 

logger=logging.getLogger()
def main():
    username='guest'
    password='guest'
    hostname=os.environ.get('hostname')
    cacert=os.environ.get('cacert')
    consumercert=os.environ.get('consumercert')
    consumerkey=os.environ.get('consumerkey')
    credentials = pika.PlainCredentials(username, password)
    tmp='na'
    #print(cacert)
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
                                    cafile=cacert
                                    )
        context.load_cert_chain(consumercert,consumerkey)
        ssl_options = pika.SSLOptions(context, "rabbitmq")
        parameters = pika.ConnectionParameters(port=5671,
                                                host=hostname,
                                                connection_attempts=5,
                                                retry_delay=5,
                                                ssl_options=ssl_options)
        connection = pika.BlockingConnection(parameters)
        logger.info("connection established with Rabbitmq at port 5671 successfully")
        channel = connection.channel()
        logger.info("successfully created channel")

    channel.queue_declare(queue='hello', durable=True)
    
    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)
        
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    while True:
        channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

    