# Monolith vs n-Tier vs Microservices

## Monolith
One codebase, one deployment — frontend, business logic, and data access all live and deploy together.

**Advantages**
- Simple to develop, test, and deploy early on
- No network overhead — everything runs in-process
- Easier to reason about for small teams/apps
- Simple local setup — one thing to run

**Disadvantages**
- Must deploy the whole app for even a small change
- Slower to start (entire app boots as one process)
- Can't scale selectively — high load on one part means scaling everything
- Gets harder to maintain as it grows (tightly coupled)
- One bug/crash can take down the whole app

---

## n-Tier (Multi-Tier)
App split into layers — typically frontend, business logic, and data — developed/deployed/scaled somewhat independently, but still one coordinated system.

**Advantages**
- App layer and database layer updated separately
- Each tier scales independently (e.g. more app servers, same database)
- Clearer separation of concerns → easier to maintain
- Easier to swap/upgrade one tier without touching the others

**Disadvantages**
- Slower to deploy than a monolith (multiple layers to coordinate)
- More moving parts — more config/infrastructure to manage
- Network communication between tiers adds latency + failure points

---

## Microservices
App broken into many small, independent services, each owning one piece of functionality, talking over the network (usually APIs).

**Advantages**
- Scale only the specific service under load
- Teams develop/deploy/update services independently
- One service failing doesn't necessarily take the whole app down
- Each service can use its own tech stack

**Disadvantages**
- Complex to build, deploy, monitor, secure
- Harder to test end-to-end (one action can span several services)
- Network latency/reliability between services is a real concern
- Needs mature DevOps (service discovery, monitoring, orchestration — Docker/Kubernetes)

---

## Quick comparison

| | Monolith | n-Tier | Microservices |
|---|---|---|---|
| Deployment | One unit, all at once | Layered, coordinated | Independent, per service |
| Scaling | Whole app only | Per tier | Per service |
| Complexity | Low | Medium | High |
| Best for | Small apps, early-stage projects | Apps needing separate app/data scaling | Large, complex systems with independent teams |
