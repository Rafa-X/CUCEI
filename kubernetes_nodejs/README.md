## Kubernetes
- ¿Qué es Kubernetes?
- ¿Qué es Ingress?
- ¿Qué es un LoadBalancer?

# Kubernetes Hello World Node.js
This project is an example of a simple deployment of kubernetes applications. <br>

Expose 2 API's:
- /current-date   - show the current date
- /fibo/:n        - implement a fibonnaci with an specified number (higher numbers could crash the server)

The last one is good to test the capacity of the cluster by implementing arithmetic operations

# Start

Build the image

```
docker build . -t rafa-x/nodejs_kubernetes
```

Run the Image

```
docker run -d -p 3000:3000 rafa-x/nodejs_kubernetes
```

# Deploying in the Kubernetes cluster

First create the Pods and the autoscale 

```
kubectl apply -f kubernetes/deployment.yml
```

Check if is OK:

```
kubectl get pods -l app=nodekub-node -o yaml | grep podIP
```

# Exposing the Api to the World:

```
kubectl apply -f kubernetes/service-external.yml
```

Checking:

```
kubectl get service
```

Run this to see the auto scaling working:

```
ab -n 500 -c 10 -s 600 http://<IP>/fibo/35
```

# Exposing the Api inside the cluster:


```
kubectl apply -f kubernetes/service-external.yml
```

Checking:

```
kubectl run terminal --generator=run-pod/v1 --image=alpine:3.8 -i --tty
```