# Local Node.js + Mongo App Deployment (k8-yaml-definitions)

## Step 1: setup

* Create folder: `local-nodejs20-app-deploy` in `/yaml-definitions`
* Copy + rename:
`nginx-deploy.yml` → `ttt-deploy.yml`
`nginx-service.yml` → `ttt-service.yaml`

* Swap labels/image/ports to match the app

## Step 2: app-only Deployment (`ttt-deploy.yml`)

```yaml
apiVersion: apps/v1  
kind: Deployment         
metadata:
  name: ttt-deploy           # name of this Deployment object
  namespace: default
spec:
  replicas: 3                 # how many pods to run
  selector:
    matchLabels:
      app: ttt         
  template:                     # the pod "blueprint"
    metadata:
      labels:
        app: ttt           
    spec:
      containers:
      - name: ttt-app          
        image: kyram6/tech610-tttapp:1.2.0   # the pushed Docker Hub image to run
        ports:
        - containerPort: 3000            # the port the app listens on inside the container
```

* `replicas: 3` — this is what gives you resilience/scaling: if one pod dies, the Deployment's
  controller notices and spins up a replacement to get back to 3

## Step 3: app-only Service (`ttt-service.yaml`)

```yaml
apiVersion: v1
kind: Service
metadata:
  name: ttt-svc
  namespace: default 
spec:
  ports:
  - nodePort: 30002     # range is 30000-32768 - the port you actually hit from your laptop/browser
    port: 3000            # the port the Service itself listens on (internal to the cluster)
    targetPort: 3000        # the port on the pod to forward traffic to - must match containerPort above

  selector:
    app: ttt               

  type: NodePort      # (other options: ClusterIP - internal only, LoadBalancer - cloud LB)
```

* `type: NodePort` is what makes this reachable from outside the cluster at all — a `ClusterIP` Service (the default) would only be reachable from other pods

## Deploy & check app only

```bash
kubectl apply -f ttt-deploy.yml    # don't forget -f
kubectl apply -f ttt-service.yaml

kubectl get pods    # confirm 3 pods, Running
kubectl get all     # confirm the NodePort is listed
```

Check `http://localhost:30002/` in the browser.

![alt text](<Screenshot 2026-07-30 at 12.49.11.png>)

## Step 4: adding Mongo

### `mongo-deploy.yml`

```yaml
apiVersion: apps/v1   
kind: Deployment        # kind of service/object you want to create
metadata:
  name: mongo-deployment   #name the deployment
spec:
  selector:
    matchLabels:
      app: mongo          
  replicas: 1    # create a replica set of this with instances/pods - just 1 for the DB
  template:
    metadata:
      labels:
        app: mongo
    spec:
      containers:
      - name: mongo
        image: mongo:8.2.5        # the maintained Mongo image - same version used in Docker Compose
        ports:
        - containerPort: 27017      # mongo's default port
```


* `image: mongo:8.2.5` — this is a maintained image - comes patched/configured

### `mongo-service.yml`

```yaml
apiVersion: v1
kind: Service
metadata:
  name: mongo-svc
  namespace: default 
spec:
  ports:
  - port: 27017
    targetPort: 27017

  selector:
    app: mongo 

  type: ClusterIP   # internal only - the app can reach it, your laptop/browser can't
```


* no `nodePort` here — Mongo shouldn't be reachable from outside the cluster, only from the app pods, so `ClusterIP` (internal-only) is used


### `ttt-deploy.yml` (updated with the DB connection)

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ttt-deployment
spec:
  selector:
    matchLabels:
      app: ttt
  replicas: 3
  template:
    metadata:
      labels:
        app: ttt
    spec:
      containers:
      - name: ttt-app
        image: kyram6/tech610-tttapp:1.2.0
        ports:
        - containerPort: 3000
        env:
        - name: MONGODB_URI
          value: "mongodb://mongo-svc:27017/ttt"
```

**Why each bit matters:**
* `env` must sit **inside** the container definition (same indent level as `image` and `ports`) 

## Deploy & check app + mongo

```bash
kubectl apply -f mongo-deploy.yml
kubectl apply -f mongo-service.yml
kubectl apply -f ttt-deploy.yml   # re-apply after adding the env block

kubectl get pods    # should show 3 ttt pods + 1 mongo pod, all Running
kubectl get all     # ttt-svc (NodePort) + mongo-svc (ClusterIP)
```

then go to `http://localhost:30002/`