#!/bin/bash
 
## TESTED: 6/7/2026
## TESTED BY: Kyram
## TESTED ON: AWS, Ubuntu 24.04 LTS, t3.micro
## AIM: Work as a script + user data on fresh Ubuntu 24.04 LTS VM
## PUPROSE: Provision the MongoDB 8.2.5 for TTT app
 
echo Update the sources list...
sudo apt-get update -y
echo Done!
 
echo Upgrade any packages available...
sudo apt-get upgrade -y
echo Done!

echo Install GBG key...
curl -fsSL https://pgp.mongodb.com/server-8.0.asc | \
   sudo gpg -o /usr/share/keyrings/mongodb-server-8.0.gpg \
   --dearmor
echo Done!

echo Create list file...
echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-8.0.gpg ] https://repo.mongodb.org/apt/ubuntu noble/mongodb-org/8.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-8.2.list
echo Done!

echo Update the sources list..
sudo apt-get update
echo Done!

echo Install MongoDB...
sudo apt-get install -y \
   mongodb-org=8.2.5 \
   mongodb-org-database=8.2.5 \
   mongodb-org-server=8.2.5 \
   mongodb-mongosh \
   mongodb-org-shell=8.2.5 \
   mongodb-org-mongos=8.2.5 \
   mongodb-org-tools=8.2.5 \
   mongodb-org-database-tools-extra=8.2.5

echo Done!

#sudo systemctl status mongod # takes up terminal 

echo Enable MongoDB...
sudo systemctl enable mongod #enable mongod
echo Done!

### 

echo Configure bindIp...
sudo sed -i 's/bindIp: 127.0.0.1/bindIp: 0.0.0.0/' /etc/mongod.conf
echo Done!

echo Start MongoDB...
sudo systemctl start mongod
echo Done!

#sudo systemctl status mongod # check if running



export MONGODB_URI=mongodb://172.31.60.67:27017/tictactoe

# npm start

# pm2 start index.js --name "tictactoe"