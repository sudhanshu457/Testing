import kopf
import kubernetes.client
from kubernetes.client.rest import ApiException
import yaml
import os
import logging
import time
# parent_dir = os.getcwd()
# path = os.path.join(parent_dir,"logs")
# os.chdir(path)
# logging.basicConfig(filename='operator.log',
#                     format='%(asctime)s %(message)s'
#                     ) 

#Creating an object 
logger=logging.getLogger() 

#Setting the threshold of logger to DEBUG 
logger.setLevel(logging.DEBUG) 
logger.info("*************logs from operator****************")
@kopf.on.create('cp.info', 'v1', 'certificateauthoritys')
def create_fn(spec, **kwargs):
    name = kwargs["body"]["metadata"]["name"]
    print("Name is %s\n" % name)
    # loading pvc
    
    logger.info("persistent volume already created")

    # loading Certificate-authority deployment
    path1 = os.path.join(os.path.dirname(__file__), 'CA-deployment.yaml')
    tmpl1 = open(path1, 'rt').read()
    data1 = yaml.safe_load(tmpl1)
    logger.info("loaded ca deployment yaml successfully")

    # loading nodeport cervice for certificate authority
    #path3 = "ca-clusterip.yaml"
    path3 = os.path.join(os.path.dirname(__file__), 'ca-clusterip.yaml')
    tmpl3 = open(path3, 'rt').read()
    data3 = yaml.safe_load(tmpl3)
    logger.info("loaded clusterIP service for certificate authority yaml successfully")

    # loading rabbitmq
    #path2 = "rabbitmq-deployment.yaml"
    path2 = os.path.join(os.path.dirname(__file__), 'rabbitmq-deployment-flask.yaml')
    tmpl2 = open(path2, 'rt').read()
    data2 = yaml.safe_load(tmpl2)
    logger.info("loaded Rabbitmq deployment yaml successfully")

    # loading nodeport service for rabbitmq
    #path4 = "rabbitmq-clusterip.yaml"
    path4 = os.path.join(os.path.dirname(__file__), 'rabbitmq-clusterip.yaml')
    tmpl4 = open(path4, 'rt').read()
    data4 = yaml.safe_load(tmpl4)
    logger.info("loaded Rabbitmq clusterIP service yaml successfully")

    # loading consumer pod secret
    #path5 = "consumer-deployment-secret.yaml"
    path5 = os.path.join(os.path.dirname(__file__), 'consumer-deployment-secret.yaml')
    tmp5 = open(path5, 'rt').read()
    data5 = yaml.safe_load(tmp5)
    logger.info("loaded consumer secret yaml successfully")
    
    # loading consumer pod
    #path6 = "consumer-deployment.yaml"
    path6 = os.path.join(os.path.dirname(__file__), 'consumer-deployment.yaml')
    tmp6 = open(path6, 'rt').read()
    data6 = yaml.safe_load(tmp6)
    logger.info("loaded consumer pod yaml successfully")

    # loading producer pod secret
    #path7 = "producer-deployment-secret.yaml"
    path7 = os.path.join(os.path.dirname(__file__), 'producer-deployment-secret.yaml')
    tmp7 = open(path7, 'rt').read()
    data7 = yaml.safe_load(tmp7)
    logger.info("loaded producer secret yaml successfully")
    
    # loading consumer pod
    #path8 = "producer-deployment.yaml"
    path8 = os.path.join(os.path.dirname(__file__), 'producer-deployment.yaml')
    tmp8 = open(path8, 'rt').read()
    data8 = yaml.safe_load(tmp8)
    logger.info("loaded producer pod yaml successfully")

    #path9 = os.path.join(os.path.dirname(__file__), 'external-deployment-secret.yaml')
    #tmp9 = open(path9, 'rt').read()
    #data9 = yaml.safe_load(tmp9)
    #logger.info("loaded external secret yaml successfully")
    
    # loading consumer pod
    #path8 = "producer-deployment.yaml"
   # path10 = os.path.join(os.path.dirname(__file__), 'external-deployment.yaml')
   # tmp10 = open(path10, 'rt').read()
   # data10 = yaml.safe_load(tmp10)
   # logger.info("loaded external pod yaml successfully")

    # #######################kubernetes dashoard###############################################
    # path11 = os.path.join(os.path.dirname(__file__), 'dashboard-admin-sa.yaml')
    # tmp11 = open(path11, 'rt').read()
    # data11 = yaml.safe_load(tmp11)
    # logger.info("loaded service account for kuberenetes dashbaord successfully")

    # path12 = os.path.join(os.path.dirname(__file__), 'cluster-role-binding.yaml')
    # tmp12 = open(path12, 'rt').read()
    # data12 = yaml.safe_load(tmp12)
    # logger.info("loaded cluster role binding for kuberenetes dashbaord successfully")

    logger.info("*********************************************************************")
    logger.info("************wait for few min until everything starts up***************")

    # Make it our child: assign the namespace, name, labels, owner references, etc.
    # Actually create an object by requesting the Kubernetes API.
    # kopf.adopt(data0)
    api1 = kubernetes.client.CoreV1Api()
    api = kubernetes.client.AppsV1Api()
    # try:
    #   obj = api1.create_namespaced_persistent_volume_claim(namespace=data0['metadata']['namespace'], body=data0)
    #   time.sleep(30)
    #   logger.info("persistent volume for storing certificates created")
    # except ApiException as e:
    #   print("Exception when calling AppsV1Api->create_namespaced_deployment: %s\n" % e)

    kopf.adopt(data1)
    
    try:
      
      depl1 = api.create_namespaced_deployment(namespace=data1['metadata']['namespace'], body=data1)
      
      # return {'children': [depl1.metadata.uid]}
      time.sleep(30)
      logger.info("ca deployment created")
    except ApiException as e:
      logger.error("Exception when calling AppsV1Api->create_namespaced_deployment: %s\n" % e)
    
    kopf.adopt(data2)
    try:
      depl2 = api.create_namespaced_deployment(namespace=data2['metadata']['namespace'], body=data2)
      # return {'children': [depl2.metadata.uid]}
      time.sleep(30)
      logger.info("rabbitmq deployment created")
    except ApiException as e:
      logger.error("Exception when calling AppsV1Api->create_namespaced_deployment: %s\n" % e)
    

    kopf.adopt(data3)
    try:
      s3=api1.create_namespaced_service(namespace=data3['metadata']['namespace'], body=data3)
      time.sleep(30)
      logger.info("clusterip service for ca created")
    except ApiException as e:
      logger.error("Exception when calling AppsV1Api->create_namespaced_service: %s\n" % e)

    kopf.adopt(data4)
    try:
      s4=api1.create_namespaced_service(namespace=data4['metadata']['namespace'], body=data4)
      time.sleep(30)
      logger.info("clusterip service for rabbitmq created")
    except ApiException as e:
      logger.error("Exception when calling AppsV1Api->create_namespaced_service: %s\n" % e)

    kopf.adopt(data5)
    try:
      s5=api1.create_namespaced_secret(namespace=data5['metadata']['namespace'], body=data5)
      time.sleep(20)
      logger.info("consumer secret created")
    except ApiException as e:
      logger.error("Exception when calling AppsV1Api->create_namespaced_service: %s\n" % e)

    kopf.adopt(data7)
    try:
      s6=api1.create_namespaced_secret(namespace=data7['metadata']['namespace'], body=data7)
      time.sleep(40)
      logger.info("producer secret created")
    except ApiException as e:
      logger.error("Exception when calling AppsV1Api->create_namespaced_service: %s\n" % e)

    #kopf.adopt(data9)
    #try:
    #  s9=api1.create_namespaced_secret(namespace=data9['metadata']['namespace'], body=data9)
     # time.sleep(40)
      #logger.info("external secret created")
    #except ApiException as e:
     # logger.error("Exception when calling AppsV1Api->create_namespaced_service: %s\n" % e)

    kopf.adopt(data6)
    try:
      p6=api.create_namespaced_deployment(namespace=data6['metadata']['namespace'], body=data6)
      time.sleep(20)
      logger.info("consumer pod created")
    except ApiException as e:
      logger.error("Exception when calling AppsV1Api->create_namespaced_pod: %s\n" % e)

    kopf.adopt(data8)
    try:
      p7=api.create_namespaced_deployment(namespace=data8['metadata']['namespace'], body=data8)
      time.sleep(20)
      logger.info("producer pod created")
    except ApiException as e:
      logger.error("Exception when calling AppsV1Api->create_namespaced_pod: %s\n" % e)
    
    #kopf.adopt(data10)
    #try:
     # p10=api.create_namespaced_deployment(namespace=data10['metadata']['namespace'], body=data10)
     # time.sleep(20)
      #logger.info("external pod created")
    #except ApiException as e:
     # logger.error("Exception when calling AppsV1Api->create_namespaced_pod: %s\n" % e)

    

    
    

    
