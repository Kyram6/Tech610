# Kubernetes
 
## Some of the biggest challenges facing enterprises
 
* modernise legacy applications
* migrating to the cloud or back to on-prem
* costs of cloud & AI use
* security & compliance
  * AI assisting with hacks
  * Need to protect data (as well as applications & services)
* understanding how they can make best use of AI
* containerisation -> Kubernetes
  
## Intro to Kubernetes
 
Kubernetes (k8s) = open source container orchestration platform

It automates:
- deploying,
- scaling
- managing containerised applications across a group of machines, instead of 
manually starting/stopping/restarting containers on individual hosts.
 
## Why is Kubernetes needed
 
Running one container with `docker run` is easy. Running hundreds of containers, across
multiple hosts, reliably, is not. Kubernetes solves problems like:
 
* what happens when a container crashes? -> k8s restarts it automatically
* how do I run more copies when traffic spikes? -> scaling (manual or auto)
* how do containers find each other? -> built-in service discovery / networking
* how do I roll out a new version without downtime? -> rolling updates + rollback
* how do I spread load across machines efficiently? -> scheduler places pods based on resources
* how do I keep secrets/config out of my container images? -> Secrets & ConfigMaps
Basically: containers solve "package and run my app the same way everywhere", Kubernetes
solves "run and manage lots of those containers, reliably, at scale".
 
## Benefits of Kubernetes
 
* Automated scaling (up/down based on demand)
* Self-healing (restarts failed containers, replaces/reschedules pods on failed nodes)
* Rolling updates and rollbacks with (near) zero downtime
* Portable across cloud providers and on-prem (avoids vendor lock-in vs a single cloud's
  proprietary container service)
* Efficient use of hardware — bin-packs workloads onto nodes rather than 1 app per VM
* Huge community — lots of tooling, managed offerings, support


### Success stories
 
* **Spotify** — migrated to k8s to run microservices at scale, automated scaling for peak
  events (album drops, live events)

* **Airbnb** — used k8s to automate deployment of microservices, each getting the resources
  it needs without manual intervention
* **The New York Times** — containerised legacy apps into a microservices setup, faster
  releases, more agility
* **Pokémon GO** — used k8s to handle the massive, unpredictable spike in demand
  at launch — classic example of why auto-scaling matters
* In conclusion: faster deployments, better hardware utilisation, more
  agility — but also a steep learning curve (YAML, new concepts) as the trade-off
  
## Kubernetes architecture
 
A cluster is split into two halves: the **control plane** (the brain, makes decisions) and the
**data plane** (the muscle, runs the actual workloads).
 
 
**Control plane components:**
* `kube-APIserver` — front door for the cluster, everything (kubectl, controllers, kubelet) - hub for all interactions, validates requests ,only component that accesses etcd
  talks to the cluster through this
* `etcd` — key-value store holding the entire cluster's state/config
* `kube-scheduler` — decides which node a new pod should run on based on resources/constraints
* `controller-manager` — constantly compares actual state to desired state and fixes drift
  (e.g. spins up a new pod if one dies)

**Data plane (worker node) components:**
* `kubelet` — agent on each node, talks to the API server, makes sure containers described
  in a pod spec are actually running
* `kube-proxy` — handles networking/load balancing rules on the node
* container runtime — actually runs the containers 
  
### The cluster setup
 
**What is a cluster** — a set of machines (nodes) grouped together and managed as one unit by
Kubernetes. At minimum: at least ONE master (control plane) node + at least ONE worker node.
* production — want a multi-node setup (multiple masters and/or workers) so there's no single
  point of failure
* dev/testing — a single-node setup is fine (see minikube below)
**Master vs worker nodes**
* master (control plane) node — runs the control plane components above, makes the decisions,
  doesn't usually run application workloads itself
* worker node — runs the actual application pods, does what the control plane tells it to
**Managed service vs launching your own**
 
Managed (EKS, GKE, AKS, etc.) — cloud provider runs the control plane for you (etcd, API
server, scheduler, patching, HA, upgrades).
* Pros: way less operational overhead, provider handles control plane HA/patching/upgrades,
  faster to get started, easier to scale
* Cons: less control/customisation, tied into that provider's ecosystem to some degree, can
  cost more at scale, still fully responsible for securing everything above the control plane
  (RBAC, network policies, pod security, images)
Self-hosted (running your own on EC2/on-prem) — you install and run every component yourself.
* Pros: full control over every component/version, can tailor exactly to requirements, no
  provider lock-in
* Cons: you own all of it — HA, upgrades, patching, backups, security — needs real in-house
  k8s expertise, higher ongoing operational effort
**AKS (Azure Kubernetes Service) specifically:**
* master node and worker nodes are kept separate
* Azure runs/manages the master node for you
* Azure doesn't charge you for the master node itself
* what you actually pay for: one VM per worker node
**Comparing to AWS & GCP:**
* with EKS or GKE — you *do* pay for the master node (roughly ~10p/hr)
* so AKS can work out cheaper on the control plane side specifically
**minikube (local dev):**
* both master and worker node run on a single VM — good for learning/testing locally,
  not for production
**Control plane vs data plane** — see diagram above: control plane makes decisions (what
should run and where), data plane actually runs the workloads and routes traffic. In managed
services, the provider owns the control plane, you own the data plane (and worker node/pod
level security is still on you).
 
## Kubernetes objects
 
* **Pod** — smallest deployable unit in k8s. One or more containers that share networking/
  storage and are always scheduled together on the same node.
* **ReplicaSet** — makes sure a specified number of identical pod replicas are running at all
  times; replaces any that die.
* **Deployment** — sits on top of ReplicaSets, manages rolling updates/rollbacks. In practice
  I define a Deployment and it manages the ReplicaSet(s)/Pods for me — I shouldn't touch a
  ReplicaSet directly.
* **Service** — stable networking endpoint/IP in front of a changing set of pods (pods come
  and go, a Service gives something consistent to talk to).
* **ConfigMap / Secret** — inject config and sensitive values into pods without baking them
  into the image.
* **Namespace** — logical partition inside a cluster, used to separate workloads/teams/envs.

  
**What does it mean a pod is "ephemeral"?**
 
Pods aren't meant to live forever — they can be killed and replaced at any time 
That's why:
* apps running in k8s should be designed to be stateless where possible
* actual state/data needs to live outside the pod — a Persistent Volume, or an external DB
* I shouldn't rely on a pod's identity/IP staying the same — that's what Services are for

---
## How to mitigate risks with containers
* use maintained container images 
* use automatic vulnerability scanning on container registry
* use own security scanning tool on your container images 
* NEVER run containers with root privileges 
* monitor and/or log of container activity 

## Maintained images 

#### What is a maintained image 
* A docker image that is regularly updated/managed by a maintainer 
* usually the maintainer is an orginisation, a community, or an individual 
  * example: canonical maintain ubuntu image 
  
### pros and cons of using maintained images for your base container images 
* better security because regularly patched 
* better stability 
* more support & doc available 
* usually they adhere to best practices/industry standards 
* may be streamlined for performance or smaller image size


## Practical: deploying nginx (Deployment + Service)
 
Deploy with a Deployment yaml first, then check it:
 
```bash
kubectl create -f nginx-deploy.yml
kubectl get deployment   # shows just deployments
kubectl get pods         # just shows pods
```
 
A Deployment on its own isn't reachable — need to expose it with a Service (a separate
object/yaml).
 
`nginx-service.yaml`:
```yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-svc
  namespace: default   # if you don't specify, it defaults to `default` - namespace is just a way to organise
spec:
  ports:
  - nodePort: 30001    # range is 30000-32768
    port: 80
    targetPort: 80
 
  selector:
    app: nginx          # this label connects this service to the deployment
 
  type: NodePort         # also can use LoadBalancer - for local use ClusterIP
```
 
Create it:
```bash
kubectl create -f nginx-service.yaml
```
 
`apply` does the same as `create` but will create it if it doesn't exist *and* can update it
if it does — safer to default to `apply`:
```bash
kubectl apply -f nginx-service.yaml   # make sure you're in the right folder
```
 
Check everything:
```bash
kubectl get all   # can now see the nodeport
```
 
Then visit `http://localhost:30001/` to see it live.


-----

increase replicas change replicas in nginx-deploy.yml best way works for me 

also

kubectl scale --current-replicas=5 --replicas=6 deployment/nginx-deployment[name of deployment]
 3 for app 

