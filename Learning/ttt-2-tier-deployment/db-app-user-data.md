# Provisioning a Mongo DB VM and App VM with User Data

## `prov-db.sh` — Database VM User Data

[Prov-db script](prov-db.sh)

```bash
#!/bin/bash

sudo apt-get update -y

sudo apt-get upgrade -y

curl -fsSL https://pgp.mongodb.com/server-8.0.asc | \
   sudo gpg -o /usr/share/keyrings/mongodb-server-8.0.gpg \
   --dearmor

echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-8.0.gpg ] https://repo.mongodb.org/apt/ubuntu noble/mongodb-org/8.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-8.2.list

sudo apt-get update

sudo apt-get install -y \
   mongodb-org=8.2.5 \
   mongodb-org-database=8.2.5 \
   mongodb-org-server=8.2.5 \
   mongodb-mongosh \
   mongodb-org-shell=8.2.5 \
   mongodb-org-mongos=8.2.5 \
   mongodb-org-tools=8.2.5 \
   mongodb-org-database-tools-extra=8.2.5

sudo sed -i 's/bindIp: 127.0.0.1/bindIp: 0.0.0.0/' /etc/mongod.conf

sudo systemctl start mongod
sudo systemctl enable mongod
```
> wait a minute or two to check status with ``` sudo systemctl status mongod ```

Key things this does: installs MongoDB, changes `bindIp` from `127.0.0.1` (localhost only) to `0.0.0.0` (accept connections from any IP — needed so the app VM can reach it), then enables and starts the `mongod` service.

## `prov-app.sh` — App VM User Data

```bash
#!/bin/bash

sudo pm2 delete all

cd /tech610-tic-tac-toe
cd app

pm2 kill
MONGODB_URI=mongodb://[PRIV DB IP]:27017/tic-tac-toe pm2 start index.js

```

## Troubleshooting

SSH into the database VM and check:
```bash
sudo systemctl status mongod        # is mongod actually running?
cat /etc/mongod.conf | grep bindIp  # did bindIp actually get changed to 0.0.0.0?
 ```

 ### Blockers?

 - PM2 port conflicts

A previous PM2 process was already running from the app image, causing an EADDRINUSE (port already in use) error.
Deleting existing PM2 processes (pm2 delete all/pm2 kill) before starting the app fixed the problem.










 ----


# Provisioning a Mongo DB VM and App VM with Images Only

## Aim

Provision a database VM and an app VM using pre-built images, so both come up ready to run with only minimal user data (just enough to point the app at the database and start it).

### Pre-requisites

- A running database VM that has been fully tested — for the Tic Tac Toe app, the frontpage works in database mode (footer shows `Persistent with Mongo DB`).

## Steps

1. Using the working database VM, create a database image.

2. Use that custom database image to launch a new database VM.

3. Use the custom app image, plus a small `run-app-only.sh` user data script, to launch a new app VM that connects to the new database VM.

4. Adjust `run-app-only.sh` to export the database connection string before pasting it into user data.

5. Once the app page comes up in database mode, post the deliverable.

## Step 1 — Create the Database Image

From the EC2 Console, with the working DB VM selected:
1. Actions → Image and templates → Create image
2. Name: `tech610-kyram-tictactoe-db-image`
3. Create image (takes a few minutes while AWS snapshots the volume)

## Step 2 — Launch a New DB VM from the Image

1. Launch instance → My AMIs → select the image just created
2. No user data needed — the image already has MongoDB installed, `bindIp` set to `0.0.0.0`, and the service enabled to start on boot
3. Once running, note its private IP (`hostname -I`, or check the EC2 console) — this will be different from the original DB VM's IP

<<<<<<< HEAD
## Step 3 — Launch the App VM from the App Image.
=======
## Step 3 — Launch the App VM from the App Image with
>>>>>>> 076301b8d554b82c8fc0a66b6fdf334ca74bb136

Since the app image already has the code and PM2 baked in, user data just needs to point it at the database and start it:

```bash
#!/bin/bash

## PURPOSE: Start TTT app pointed at Mongo DB VM, using pre-built app image + user data only

export MONGODB_URI=mongodb://<new-db-vm-private-ip>:27017/tic-tac-toe

sudo pm2 delete all

cd /tech610-tic-tac-toe/app

pm2 kill
MONGODB_URI=$MONGODB_URI pm2 start index.js
```

Replace `<new-db-vm-private-ip>` with the priv IP from DB.

Notes:
- `export MONGODB_URI=...` satisfies the task's explicit requirement to export the connection string.
- The inline `MONGODB_URI=$MONGODB_URI pm2 start index.js` is what actually guarantees PM2 picks up the variable reliably (plain `export` followed by a separate `pm2 start` was found to be unreliable in earlier testing).
- `sudo pm2 delete all` clears out any pre-existing root-owned PM2 process baked into the app image, avoiding the `EADDRINUSE` port conflict seen in earlier testing.
- remember Database security group allows app VM → port 27017

## Step 4 — Check the App

Open the app VM's public IP/URL in the browser. The footer should show:
```
Mode: Persistent with Mongo DB
```
----

## What to expect when launching app VM with user data

How long to expect before app runs? approx. 4min

1. An error (not being able to connect)
1. NGINIX home page (rev proxy has not started)
1. 502 error: bad gateway (rev proxy has started working, but app isnt running yet)
1. app display 
