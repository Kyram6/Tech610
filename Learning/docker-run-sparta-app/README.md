# Running the Sparta Node.js App in a Docker Container
- [Running the Sparta Node.js App in a Docker Container](#running-the-sparta-nodejs-app-in-a-docker-container)
  - [Objective](#objective)
  - [Step 1 — Create a Folder for This Task](#step-1--create-a-folder-for-this-task)
  - [Step 2 — Add the App Folder](#step-2--add-the-app-folder)
  - [Step 3 — Create the Dockerfile](#step-3--create-the-dockerfile)
  - [Step 4 — Build the Image](#step-4--build-the-image)
  - [Step 5 — Run the Container](#step-5--run-the-container)
  - [Step 6 — Push to Docker Hub](#step-6--push-to-docker-hub)
  - [Deliverable](#deliverable)
  - [Blockers](#blockers)
    - [1. Nested app folder](#1-nested-app-folder)
    - [2. `npm ci` failing on `postinstall` script](#2-npm-ci-failing-on-postinstall-script)

## Objective

Run the Sparta Tic Tac Toe Node.js app in a Docker container, and push the built image to Docker Hub.

---

## Step 1 — Create a Folder for This Task

Kept consistent with how other course learning is organised (under `Tech610/Learning/`), and Docker only allows one Dockerfile per folder, so this exercise gets its own subfolder:

```bash
cd /Users/kyramngoma/Github/Tech610/Learning
mkdir docker-run-sparta-app
cd docker-run-sparta-app
```
---

## Step 2 — Add the App Folder

```bash
cp -r /Users/kyramngoma/Downloads/tictactoeapp ./app
```

**Why:** the Dockerfile needs the actual app code (`package.json`, `index.js`, etc.) sitting inside this folder so it can be copied into the image during the build.

---

## Step 3 — Create the Dockerfile

```bash
touch Dockerfile
nano Dockerfile
```

**Choosing a base image**

Considered `node:20-slim` vs `node:20-alpine`. Went with `slim`:
- `alpine` is smaller, but uses `musl` instead of `glibc`, which can cause compatibility issues with native npm packages
- `slim` is still lightweight but gives fewer chances of a weird compatibility issue
(looked up the difference and asked ai which would be better and why )

Final Dockerfile:

```dockerfile
# FROM which image
FROM node:20-slim

# set working dir to "app" folder in container
WORKDIR /app

# copy package.json package-lock.json only
COPY app/package.json app/package-lock.json ./

# run npm ci for production 
RUN npm ci --omit=dev --ignore-scripts

# set working dir to "app" folder in container
WORKDIR /app

# COPY . .
COPY app/ .

# use "node" user
USER node

# expose app on port 3000
EXPOSE 3000

# run the node app using index.js
CMD ["node", "index.js"]
```

**Why each part matters:**
- `package.json` / `package-lock.json` are copied and `npm ci` run **before** the rest of the app code — so Docker can reuse the cached dependency-install layer on rebuilds if only app code changes, not dependencies
- `--ignore-scripts` — added after hitting a build failure (see Blockers) caused by the app's `postinstall` script trying to run before the rest of the code existed in the image - 
- `USER node` — switches from root to the non-privileged `node` user for better security
- `EXPOSE 3000` — documents which port the container listens on (doesn't actually publish it — that's done at `docker run` with `-p`)

and the order
1. dependencies 
2. build as required 
3. run time stageb 

---

## Step 4 — Build the Image

```bash
docker build -t kyram6/tech610-tttapp:1.2.0 .
```

- `-t` — tags the image as `<dockerhub-username>/<repo-name>:<version>`
- `.` — current directory as the build context

Verify:
```bash
docker images
```

---

## Step 5 — Run the Container

```bash
docker run -d -p 3000:3000 kyramn/tech610-tttapp:1.2.0
```

(Stop and remove any existing container using port 3000 first if needed — `docker ps`, then `docker stop`/`docker rm`.)

Check it's working:
```
http://localhost:3000
```

---

## Step 6 — Push to Docker Hub

```bash
docker login
docker push kyramn/tech610-tttapp:1.2.0
```

Then re-ran the container from the pushed image to confirm it works:
```bash
docker run -d -p 3000:3000 kyramn/tech610-tttapp:1.2.0
```

---

## Deliverable

Command anyone can use to run this image:

```bash
docker run -d -p 3000:3000 kyramn/tech610-tttapp:1.2.0
```

---

## Blockers

### 1. Nested app folder

`cp -r` copied the whole `app` source folder *into* the already-created `app` destination folder, creating `app/app/...` instead of the files sitting directly in `app/`.

**Fix:**
```bash
mv app app-temp
mv app-temp/app app
rm -rf app-temp
ls app
```

This is the same nesting pattern hit earlier in the Jenkins CI/CD task — `cp -r`/`scp -r` copying a folder *into* an existing folder of the same name always creates this doubled structure. Worth remembering for any future copy step.

### 2. `npm ci` failing on `postinstall` script

Build failed with:
```
Error: Cannot find module '/app/seeds/seed.js'
```

**Why:** the app's `package.json` has a `postinstall` script that runs `node seeds/seed.js`. At the point `npm ci` runs, only `package.json`/`package-lock.json` had been copied into the image — the `seeds` folder didn't exist yet (it's copied later in `COPY app/ .`), so the script failed.

**Fix:** added `--ignore-scripts` to the `npm ci` command, since the seed script wasn't required for the app to run:
```bash
RUN npm ci --omit=dev --ignore-scripts
```
-------
[README for docker compose of deploying app and database](../docker-compose-ttt/README.md)