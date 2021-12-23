Prerequisites:
- Minikube or Docker-Desktop with kubernetes enabled
- kopf - pip install kopf kubernetes
(OR)
-gke cluster

Note: kindly use your docker username and update your username in the code files wherever required

Certificate authority:
creates certificate for Rabbitmq, consumer, producer, and CA using openssl tool.
It provides API for creating unique token and can be access at port 30000 through browser localhost

Rabbitmq:
It is a message broker used by services to communicate securely with each other.

Consumer and Producer:
Depicts a simple application using Rabbitmq for communication.

Operator:
It helps in automating the process of executing all files.

CertificateAuthority, Producer, consumer, Rabbitmq are all together using persistent volume.

If using wsl2 one can see those certificates at \\wsl$\docker-desktop-data\version-pack\community\k8s-pvc-{pvc-name}


Building the application:
1. Creating persistent volume
    kubectl apply -f dynamic-pvc.yaml

2. Building Certificate authority
    -- build image in certificate-authority folder
       docker build -t <image-name> .
       docker push <image-name>
       
3. Building Rabbitmq
    -- build image in Rabbitmq folder
       docker build -t <image-name> .
       docker push <image-name>

4. Building Consumer
    -- build image in consumer folder
       docker build -t <image-name>.
       docker push <image-name>

5. Building Producer
    -- build image in producer folder
       docker build -t <image-name> .
       docker push <image-name>
       
6. Update the image names ans tags in the deployment files of these applications in /operator

7. Building Operator 
    -- build image in operator folder
       docker build -t <image-name> .
       docker push <image-name>

Move to operator folder to run 8-10 commands

8. Create customResourseDefinition
    kubectl apply -f crd.yaml

9. create object of customResource
    kubectl apply -f obj.yaml

10. Create obj of Operator 
    kubectl apply -f operator-deployment.yaml


******************accessing through kubernetes dashboard***********************
kubectl apply -f k8s-dashboard.yaml
kubectl apply -f dashboard-admin-sa.yaml
kubectl apply -f  cluster-role-binding.yaml
kubectl get secrets
kubectl describe secret dashboard-admin-sa-token-8j6cz
kubectl proxy

browser:
http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/

http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/#/overview?namespace=default


eyJhbGciOiJSUzI1NiIsImtpZCI6InVPdWw5UDU1cEkwWkhHOFFfcm9RZG43THJTS1FNRV95YUIwWDRsSlBKM00ifQ.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJrdWJlcm5ldGVzLWRhc2hib2FyZCIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VjcmV0Lm5hbWUiOiJkYXNoYm9hcmQtYWRtaW4tc2EtdG9rZW4taGtidjciLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC5uYW1lIjoiZGFzaGJvYXJkLWFkbWluLXNhIiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZXJ2aWNlLWFjY291bnQudWlkIjoiMmY1NzFlYmQtZDhlZi00NzM3LWJjZjEtODBlYjQ4ODU5MTQyIiwic3ViIjoic3lzdGVtOnNlcnZpY2VhY2NvdW50Omt1YmVybmV0ZXMtZGFzaGJvYXJkOmRhc2hib2FyZC1hZG1pbi1zYSJ9.LzCispQd-EsEsd0SE-XXq5yd9ZGM8JIwuuT2tgAqIaywvxNX9a2ykeGaPc64Xfbu40b78qRtfxpJlXbRjrEP8Ybw4JafD-H4ntldFwohCJGNFSUllIooOPWBRJpJoYSyB4IfG35l6UiHfsko1s_wS_I8-PaCHVyVI7eG36PBD1RTHpUiKE3W81qt_V4awmHKLvj_27pWrQvPH6N_3IuEIPwXElNXqy3hkwEzj-Y4uh4xhO0HWns_GsMwoJyfNXOsIrBmNHEGpfbz2VvTFsPhk0IYOmsD9zWzdpA_MDCdIoqkJLMW6mR-pwSjL3MYqIevXIJpMGCtBa4JOwyFHBumxA

****************************logger-ElasticSearch-Kibana*********************************
- move to logger folder
1. create a pod and service for Elastic search
    kubectl apply -f logger-pvc.yaml
    kubectl apply -f elk-service.yaml
    kubectl apply -f elk-stateful.yaml
    kubectl

2. create a pod and service for kibana dashboard
    kubectl apply -f kibana-service.yaml
    kubectl apply -f kibana-deploymemt.yaml

3. create a daemonset for fluentd
    kubectl apply -f fluentd-daemonset-elasticsearch-rbac.yaml

4. localhost:30005 - elasticsearch service config displayed

5. localhost:30003 - kibana dashboard.

*****************************************************************************************

kubectl delete all --all -n kubernetes-dashboard


