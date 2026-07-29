# Docker Compose - Sparta Tic Tac Toe
- [Docker Compose - Sparta Tic Tac Toe](#docker-compose---sparta-tic-tac-toe)
  - [Objective](#objective)
  - [What Is Docker Compose, and Why Use It?](#what-is-docker-compose-and-why-use-it)
  - [Step 1 — Create the MongoDB Service and Test It Alone](#step-1--create-the-mongodb-service-and-test-it-alone)
  - [Step 2 — Add the App Service](#step-2--add-the-app-service)
  - [Step 3 — Understand the Volume](#step-3--understand-the-volume)
  - [If you remove the container anything stored inside the container filesystem is gone.](#if-you-remove-the-container-anything-stored-inside-the-container-filesystem-is-gone)
  - [Step 4 — Confirm the App-Database Connection](#step-4--confirm-the-app-database-connection)
  - [Step 5 — Seed the Database](#step-5--seed-the-database)
  - [Step 6 — Other Automatic Seeding Methods to Try](#step-6--other-automatic-seeding-methods-to-try)
  - [Troubleshooting / Blockers Encountered](#troubleshooting--blockers-encountered)
    - [Port 3000 Already Allocated](#port-3000-already-allocated)
    - [YAML Parsing Error](#yaml-parsing-error)
    - [Dependency Cycle](#dependency-cycle)

## Objective

Deploy the Sparta Tic Tac Toe application and MongoDB database using Docker Compose.

The deployment consists of:

- MongoDB container
- Node.js Tic Tac Toe application container

Docker Compose allows both containers to be started with a single command.

## What Is Docker Compose, and Why Use It?

Docker Compose is a tool for defining and running multiple containers together from one config file (`docker-compose.yml` / `docker-compose.yaml`), instead of running several `docker run` commands by hand.

Without Compose, running this app would mean: start the MongoDB container manually, wait for it to be ready, start the app container manually, set its environment variables manually, and make sure the two are linked together — all separate steps, in the right order, every time.

With Compose, all of that is described once in the file, and one command handles it:

```bash
docker compose up -d
```

---

## Step 1 — Create the MongoDB Service and Test It Alone

Start with just the database service confirming it works before adding the app. (working in an agile way)

```yaml
services:
  mongodb:
    image: mongo:8.2.5
    container_name: mongodb
    ports:
      - "27017:27017"
    volumes:
      - mongodb_data:/data/db

volumes:
  mongodb_data:
```

Run:

```bash
docker compose up -d
docker ps
```

Troubleshoot with:

```bash
docker logs mongodb
```

---

## Step 2 — Add the App Service 
[README for creating app container](../docker-run-sparta-app/README.md)

```yaml
services:
  mongodb:
    image: mongo:8.2.5
    container_name: mongodb
    ports:
      - "27017:27017"
    volumes:
      - mongodb_data:/data/db

  app:
    image: kyram6/tech610-tttapp:1.2.0
    container_name: ttt-app
    ports:
      - "3000:3000"
    environment:
      MONGODB_URI: mongodb://mongodb:27017/tictactoe
    depends_on:
      - mongodb

volumes:
  mongodb_data:
```

**What each part of the file is doing:**

- **`services`** — defines the containers to run. This project has two: `mongodb` and `app`.
  
- **`container_name`** — gives each container a fixed, predictable name (`mongodb`, `ttt-app`) rather than a random Docker-generated one. This matters because the app's connection string refers to the database by that name, not an IP address 
  
- **`ports: "27017:27017"` / `"3000:3000"`** — maps a port on the host machine to the matching port inside the container.
- **`volumes: mongodb_data:/data/db`** — creates a named volume so MongoDB's data survives a container restart or removal, rather than being wiped each time.
- **`environment: MONGODB_URI`** — the connection string the app uses to reach the database, built from the container name rather than an IP:

  ```
  mongodb://mongodb:27017/tictactoe
              │        │       │
          container   port   database
            name                name
  ```

- **`depends_on: - mongodb`** — tells Compose to start `mongodb` before `app`, since the app needs the database available (or at least started) before it tries to connect.

Run both:

```bash
docker compose up -d
docker logs ttt-app
```

Confirm the app started:

```
Server running at http://localhost:3000
```

---

## Step 3 — Understand the Volume

A volume stores data outside of the container so the data is not lost when the container is deleted or recreated.

```
Container
   |
   └── App + Database files
```

If you remove the container anything stored inside the container filesystem is gone.
---

## Step 4 — Confirm the App-Database Connection

Check `docker logs ttt-app` for the app confirming the connection itself:

```
"message":"Mongo connection established","mongoTarget":"mongodb:27017/tictactoe"
```

---

## Step 5 — Seed the Database 

```bash
docker exec -it ttt-app node seeds/seed.js
```

**What each part of that command does:**
- `docker exec` — runs a command inside an already-running container, without needing to SSH into it
- `-it` — interactive terminal, so the output shows in the shell
- `ttt-app` — the container to run it in
- `node seeds/seed.js` — the actual command being run inside that container

Expected output:

```
Seeded active app state via /api/seed (10 records).
```

---

## Step 6 — Other Automatic Seeding Methods to Try

- **Init script method** — mount a script into `/docker-entrypoint-initdb.d/` so MongoDB seeds itself automatically the moment the container starts, with no manual trigger at all.
- **Separate seed container** — add a third service in `docker-compose.yaml` that runs once and exits, dedicated purely to seeding.
- **Startup-command method** — override the app container's start command so it seeds itself the moment it starts, instead of running `docker exec` by hand:

  ```yaml
  command: sh -c "node index.js & sleep 5 && node seeds/seed.js && wait"
  ```

  Breaking this down:
  - `node index.js &` — starts the app in the background (`&`) so the next commands can still run
  - `sleep 5` — gives the app a few seconds to finish starting and connect to MongoDB before seeding
  - `node seeds/seed.js` — runs the same seed script, but automatically rather than via a manual `docker exec`
  - `wait` — keeps the shell (and container) alive after seeding, since the container exits once its main process ends

  This would make seeding fully automatic — no manual step at all after `docker compose up -d`.

---

## Troubleshooting / Blockers Encountered

### Port 3000 Already Allocated

**What happened:** the app container failed to start because port 3000 was already being used by a leftover container from an earlier test.

**Why:** an old container was still running and holding the port.

**Fix:**

```bash
docker ps

docker stop [container name/id]
docker rm [container name/id]

docker compose down
```

### YAML Parsing Error

**What happened:** while editing the compose file, hit a parsing error:

```
yaml: while parsing a block mapping at <unknown position>: line 7, column 2: did not find expected key
```

**Why:** indentation mistake in the YAML — a key wasn't nested correctly under its parent.

**Fix:** corrected the indentation and confirmed the file was valid with `docker compose config` before running it again.

### Dependency Cycle

**What happened:** after a Docker Desktop restart stopped all containers, brought them back up and hit:

```
dependency cycle detected: mongodb -> mongodb
```

**Why:** I accidentally placed the `environment` and `depends_on` under the `mongodb` service instead of the `app` service — so Compose read it as "mongodb depends on mongodb."

**Fix:** moved `environment` (the `MONGODB_URI`) and `depends_on` to the `app` service, where they belong 