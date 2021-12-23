import os
from subprocess import call
import logging
import time
# logging.basicConfig(filename="/app/logs/ca.log", 
#                     format='%(asctime)s %(message)s') 

logger=logging.getLogger()
#Setting the threshold of logger to DEBUG 
logger.setLevel(logging.DEBUG)
directory = "new_certs"
parent_dir = os.getcwd()
path1 = os.path.join(parent_dir, directory) 



try:
    directory ="Trusted-CA"
    path2=os.path.join(path1,directory)
    os.mkdir(path2)
    os.chdir(path2)
    decrypted = call(['openssl', 'genrsa', '-out', 'CA-key.pem', '2048'])
    decrypted = call(['openssl' , 'req' , '-new', '-key',  'CA-key.pem',  '-x509',  '-days',  '1000' ,'-out', 'CA-cert.pem', '-subj', "/C=US/ST=NRW/L=Earth/O=CAserver/OU=IT/CN=rabbitmq/emailAddress=email@example.com"]) 
    logger.info("CA certificates created successfully")
except FileExistsError:
    logger.warning("Certificate already exist for CA.")


try:
    directory ="Rabbitmq-server-certificate"
    path=os.path.join(path1,directory)
    os.mkdir(path)
    os.chdir(path)
    decrypted = call(['openssl', 'genrsa', '-out', 'server-key.pem', '2048'])
    decrypted = call(['openssl' , 'req' , '-new','-key',  'server-key.pem', '-out','server-signingReq.csr','-subj', "/C=US/ST=NRW/L=Earth/O=Rabbitserver/OU=IT/CN=rabbitmq/emailAddress=email@example.com"])
    decrypted = call(['openssl' , 'x509', '-req', '-days',  '365' , '-in' , 'server-signingReq.csr', '-CA', '/app/new_certs/Trusted-CA/CA-cert.pem', '-CAkey', '/app/new_certs/Trusted-CA/CA-key.pem', '-CAcreateserial', '-out', 'server-cert.pem']) 
    logger.info("RabbitMQ certificates created successfully")
except FileExistsError:
    logger.warning("Certificate already exist for Rabbitmq.")

try:
    directory ="consumer-server-certificate"
    path=os.path.join(path1,directory)
    os.mkdir(path)
    os.chdir(path)
    decrypted = call(['openssl', 'genrsa', '-out', 'consumer-key.pem', '2048'])
    decrypted = call(['openssl' , 'req' , '-new','-key',  'consumer-key.pem', '-out','consumer-signingReq.csr','-subj', "/C=US/ST=NRW/L=Earth/O=Consumer/OU=IT/CN=rabbitmq/emailAddress=email@example.com"])
    decrypted = call(['openssl' , 'x509', '-req', '-days',  '365' , '-in' , 'consumer-signingReq.csr', '-CA', '/app/new_certs/Trusted-CA/CA-cert.pem', '-CAkey', '/app/new_certs/Trusted-CA/CA-key.pem', '-CAcreateserial', '-out', 'consumer-cert.pem'])
    logger.info("Consumer certificates created successfully")
except FileExistsError:
    logger.warning("Certificate already exist for consumer.")

try:
    directory ="producer-server-certificate"
    path=os.path.join(path1,directory)
    os.mkdir(path)
    os.chdir(path)
    decrypted = call(['openssl', 'genrsa', '-out', 'producer-key.pem', '2048'])
    decrypted = call(['openssl' , 'req' , '-new','-key',  'producer-key.pem', '-out','producer-signingReq.csr','-subj', "/C=US/ST=NRW/L=Earth/O=Rabbitserver/OU=IT/CN=rabbitmq/emailAddress=email@example.com"])
    decrypted = call(['openssl' , 'x509', '-req', '-days',  '365' , '-in' , 'producer-signingReq.csr', '-CA', '/app/new_certs/Trusted-CA/CA-cert.pem', '-CAkey', '/app/new_certs/Trusted-CA/CA-key.pem', '-CAcreateserial', '-out', 'producer-cert.pem'])
    logger.info("Producer Certificates created successfully")
except FileExistsError:
    logger.warning("Certificate already exist for producer.")

try:
    directory ="external-server-certificate"
    path=os.path.join(path1,directory)
    os.mkdir(path)
    os.chdir(path)
    decrypted = call(['openssl', 'genrsa', '-out', 'external-key.pem', '2048'])
    decrypted = call(['openssl' , 'req' , '-new','-key',  'external-key.pem', '-out','external-signingReq.csr','-subj', "/C=US/ST=NRW/L=Earth/O=externalserver/OU=IT/CN=rabbitmq/emailAddress=email@example.com"])
    decrypted = call(['openssl' , 'x509', '-req', '-days',  '365' , '-in' , 'external-signingReq.csr', '-CA', '/app/new_certs/Trusted-CA/CA-cert.pem', '-CAkey', '/app/new_certs/Trusted-CA/CA-key.pem', '-CAcreateserial', '-out', 'external-cert.pem'])
    logger.info("Producer Certificates created successfully")
except FileExistsError:
    logger.warning("Certificate already exist for external.")



os.chdir(parent_dir)

decrypted = call(['python3','app.py'])

