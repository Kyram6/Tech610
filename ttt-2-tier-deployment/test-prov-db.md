
  1. create new instance
  1. ubuntu server 24.04 
  1. scp -i ~/.ssh/kyram-tech610-key.pem /Users/kyramngoma/Github/Tech610/Learning/ttt-2-tier-deployment/prov-db.sh ubuntu@52.17.132.107:/home/ubuntu/
  1. ssh -i ~/.ssh/kyram-tech610-key.pem ubuntu@52.17.132.107
  1. chmod +x prov-db.sh
./prov-db.sh
1. sudo systemctl status mongod - confirmed running
1. systemctl is-enabled mongod - confirmed enabled
1.  sudo cat /etc/mongod.conf | grep bindIp - verify bindIP is set correctly 

####
1. launch fresh app VM

1. scp -i ~/.ssh/kyram-tech610-key.pem /Users/kyramngoma/Tech610/Cloud/tiktaktoe.sh ubuntu@108.131.154.28:/home/ubuntu/
1. scp -i ~/.ssh/kyram-tech610-key.pem ~/Downloads/nodejs20-sparta-tictactoe-v1-2.zip ubuntu@108.131.154.28:/home/ubuntu/
1. run tictactoe.sh  (did it manually to test first)
1. export MONGODB_URI=mongodb://172.31.60.67:27017/tic-tac-toe
1. pm2 kill 
1. pm2 start index.js

# 🎮 Tic Tac Toe — 2-Tier Deployment

> Provisioning a MongoDB database VM and a Node.js app VM on AWS, connected via a private-network `MONGODB_URI`, so game data persists instead of running in-memory.

## Overview

| | |
|---|---|
| **Architecture** | 2-tier (App VM ⇄ DB VM) |
| **OS** | Ubuntu Server 24.04 LTS |
| **Database** | MongoDB 8.2.5 |
| **App runtime** | Node.js 20 + PM2 |
| **Reverse proxy** | nginx |

---

## 🗄️ Database VM Setup

### 1. Create new instance
Launched a fresh EC2 VM to host MongoDB, so the provisioning script could be tested from a clean state rather than an already-configured machine.

### 2. Ubuntu Server 24.04
Chosen to match the MongoDB repo (`noble`) used in `prov-db.sh`, and is the LTS version specified for this task.

### 3. Copy the provisioning script to the VM
```bash
scp -i ~/.ssh/kyram-tech610-key.pem \
  /Users/kyramngoma/Github/Tech610/Learning/ttt-2-tier-deployment/prov-db.sh \
  ubuntu@52.17.132.107:/home/ubuntu/
```
Copies `prov-db.sh` from the local machine to the DB VM using the SSH key for authentication.

### 4. SSH into the DB VM
```bash
ssh -i ~/.ssh/kyram-tech610-key.pem ubuntu@52.17.132.107
```
Connects into the VM to run the script and inspect the results directly.

### 5. Make the script executable
```bash
chmod +x prov-db.sh
```
Without this, Bash won't allow the script to run with `./`.

### 6. Run the script
```bash
./prov-db.sh
```
Updates the system, installs MongoDB 8.2.5, sets `bindIp` to `0.0.0.0` so it accepts connections from outside the VM (not just localhost), and starts/enables the `mongod` service.

### 7. Confirm MongoDB is running
```bash
sudo systemctl status mongod
```
✅ Confirmed running — proves the install and start steps worked.

### 8. Confirm MongoDB is enabled on boot
```bash
systemctl is-enabled mongod
```
✅ Confirmed enabled — MongoDB will auto-start after a VM restart, a core requirement of the task.

### 9. Verify the bindIp config
```bash
sudo cat /etc/mongod.conf | grep bindIp
```
✅ Confirmed `bindIp: 0.0.0.0` — proves the `sed` command in the script actually took effect.

---

## 🖥️ App VM Setup

### 1. Launch fresh app VM
A second, separate EC2 instance for the Node.js app, kept apart from the DB VM so each tier can be provisioned and tested independently.

### 2. Copy over files
```bash
scp -i ~/.ssh/kyram-tech610-key.pem \
  /Users/kyramngoma/Tech610/Cloud/tiktaktoe.sh \
  ubuntu@108.131.154.28:/home/ubuntu/
```
Copies the actual app provisioning script (`tiktaktoe.sh`) — installs Node, nginx, and pm2, and starts the game server.

```bash
scp -i ~/.ssh/kyram-tech610-key.pem \
  ~/Downloads/nodejs20-sparta-tictactoe-v1-2.zip \
  ubuntu@108.131.154.28:/home/ubuntu/
```
A zipped copy of the app code, as a backup/alternative to `git clone`.

### 3. Run the app script manually first
```bash
./tictactoe.sh
```
Ran by hand rather than trusting it blind, so each step's output could be checked and errors (like an incorrect `cd` path) caught before relying on it as an automated script.

### 4. Set the database connection string
```bash
export MONGODB_URI=mongodb://172.31.60.67:27017/tic-tac-toe
```
`172.31.60.67` is the DB VM's **private IP**, `27017` is Mongo's default port, and `tic-tac-toe` is the database name the app reads/writes to.

### 5. Reset and start the app with PM2
```bash
pm2 kill
pm2 start index.js
```
`pm2 kill` clears any existing process/daemon to avoid conflicts from a previous run (e.g. the app already running without `MONGODB_URI` set).

> ⚠️ **Note:** for `MONGODB_URI` to be reliably picked up by the spawned process, pass it inline on the same line as the start command, and save the process list so it survives a reboot:
> ```bash
> MONGODB_URI=mongodb://172.31.60.67:27017/tic-tac-toe pm2 start index.js --name tictactoe
> pm2 save
> ```
