

Virtualisation containers docker · MD
# Virtualisation, Containerisation, Microservices & Docker
 
## Differences Between Traditional, Virtualised, and Containerised Deployment
 
**Traditional deployment**
- One physical server runs one application directly on the "bare metal" OS
- To run multiple, separate applications, you'd typically need a separate physical server for each — mixing unrelated apps on one machine risked conflicts (different dependency versions, one app crashing and affecting others, resource contention)
- Most servers sat underused most of the time, since each was provisioned for its peak load "just in case"
- Scaling meant physically buying and racking new hardware — slow and expensive
**Virtualised deployment**
- A **hypervisor** sits on top of the physical hardware and splits one physical server into multiple isolated **virtual machines (VMs)**
- Each VM has its own full guest OS, virtual hardware, and runs applications independently of the others
- Much better hardware utilisation than traditional deployment — no need for a separate physical box per application
- Still relatively heavy — each VM carries the overhead of a full OS
**Containerised deployment**
- Multiple **containers** run on a single host OS, sharing the host's kernel rather than each having their own full OS
- Only the application and its dependencies are packaged — no separate guest OS per container
- Much lighter and faster to start than VMs (seconds vs minutes)
- Easier to scale and more portable — "runs the same everywhere"
dock
## What's Usually Included
 
**Virtual Machine**
- A full guest operating system (kernel + OS files)
- Virtual hardware (virtual CPU, memory, disk, network interface)
- The application and its dependencies
**Container**
- The application
- Just the dependencies/libraries the app needs
- No separate OS — it shares the host machine's kernel
This is why containers are much lighter and start much faster than VMs — there's no OS to boot, just a process to start.
 
## Benefits of Each
 
**Virtual Machines (especially over traditional physical architecture)**
- Multiple isolated environments on one physical machine — better hardware utilisation than one app per physical server
- Strong isolation — a VM crash doesn't affect other VMs on the same host
- Can run different operating systems side by side on the same hardware
- Easier disaster recovery — a VM can be snapshotted/restored as a whole

**Containers**
- Much lighter and faster to start than VMs (seconds vs minutes)
- More efficient use of resources — no duplicate OS overhead per app
- Highly portable — "runs the same everywhere," since the container packages the app with everything it needs
- Easier to scale horizontally — spin up many container instances quickly

## Microservices
 
**What are they?**
An architectural style where an application is built as a collection of small, independent services, each responsible for one specific piece of functionality, rather than one large single codebase (a "monolith").
 
**How are they made possible?**
- Containerisation (like Docker) makes it practical to package and run each small service independently
- Each microservice can be deployed, scaled, and updated on its own, communicating with others over the network (commonly via APIs)
- Orchestration tools (e.g. Kubernetes) help manage many microservices running together

**Benefits**
- Teams can work on and deploy different services independently, without waiting on the whole application to be rebuilt
- Easier to scale just the parts of the system that need it, rather than the whole application
- A failure in one service doesn't necessarily bring down the entire application
- Different services can use different languages/technologies where it makes sense


## Docker
 
**What is it?**
A platform for building, running, and managing containers — the most widely used containerisation tool.
 
**Why Docker?**
- Makes containers accessible and easy to use with a simple CLI and consistent tooling
- Huge ecosystem — prebuilt images available via Docker Hub
- Strong community support and widespread industry adoption, making it something of a standard

**Alternatives**
- **Podman** — daemonless, considered a more secure drop-in alternative
- **containerd** — a lower-level container runtime (Docker itself uses this under the hood)
- **CRI-O** — built specifically for Kubernetes
- **LXC/LXD** — lower-level Linux container tools, predating Docker

**How It Works (Docker Architecture/API)**
- **Docker Client** — the CLI you interact with (`docker run`, `docker build`, etc.)
- **Docker Daemon (dockerd)** — runs in the background, does the actual work of building/running/managing containers
- **Docker Images** — read-only templates used to create containers, built from a `Dockerfile`
- **Docker Containers** — running instances of an image
- **Docker Registry** — stores images (Docker Hub is the most well-known public registry)
- The Docker Client talks to the Docker Daemon via a REST API, which then manages images/containers/networks/volumes

**Success Story Using Docker**
- Used widely across the industry — companies like Spotify and PayPal have used Docker/containerisation to break monolithic applications into microservices, enabling faster deployments and easier scaling
- A commonly cited example: **PayPal** migrated many of its services to a containerised microservices architecture, reporting significantly reduced build/deploy times compared to their previous setup
 

