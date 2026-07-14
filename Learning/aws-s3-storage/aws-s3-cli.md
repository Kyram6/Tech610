# Manipulate AWS S3 storage 

- [Manipulate AWS S3 storage](#manipulate-aws-s3-storage)
  - [What is S3 storage](#what-is-s3-storage)
  - [ssh in](#ssh-in)
  - [Updates and Upgrades](#updates-and-upgrades)
  - [Installing AWS CLI on ubuntu 24.04 LTS](#installing-aws-cli-on-ubuntu-2404-lts)
  - [AWS CLI commands to manipulate S3 storage](#aws-cli-commands-to-manipulate-s3-storage)
    - [List whats on aws](#list-whats-on-aws)
    - [Gives commands](#gives-commands)
    - [Create bucket](#create-bucket)
    - [List whats in bucket](#list-whats-in-bucket)
    - [Uploading file to AWS bucket](#uploading-file-to-aws-bucket)
  - [making new folder to upload](#making-new-folder-to-upload)
    - [Use history to perform command](#use-history-to-perform-command)
    - [⚠️ Removing a file from bucket](#️-removing-a-file-from-bucket)
    - [⚠️ Delete multiple files in bucket](#️-delete-multiple-files-in-bucket)
    - [⚠️Delete a bucket with files in it](#️delete-a-bucket-with-files-in-it)
- [What is Boto3](#what-is-boto3)
  - [Boto3 Scripts](#boto3-scripts)
  - [purpose of todays tasks](#purpose-of-todays-tasks)


<br>

## What is S3 storage 
- simple storage service 
  
- used to store and retrieve any amount, at any time, frome anywhere 
  
- can be easily be used to host a static website on the cloud
- Provides built in redudancy by default 
  - 3 copies - each one stored across the AZ's in region 
- Access from AWS console, AWS CLI & Pytho Boto3 
- often the resources for an application/website are stored in S3 e.g images 
- default is files you put there are private, you need to configure to make public.






---- 
move - mv ~/Downloads/tech610-kngoma_accessKeys.csv ~/.ssh/

## ssh in 
```
ssh -i ~/.ssh/kyram-tech610-key.pem ubuntu@[ec2-XX-XXX-XX-XX].eu-west-1.compute.amazonaws.com
```
## Updates and Upgrades 
```
sudo apt-get update -y
sudo apt-get upgrade -y 
sudo apt-get install unzip
```

## Installing AWS CLI on ubuntu 24.04 LTS

```
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```

Check your version with 
```
aws --version
```

Autheticate with credentials 
```
aws configure 
```

* AWS Access Key ID [None]: Access key ID

* AWS Secret Access Key [None]: Secret access key

* Default region name [None]: eu-west-1

* Default output format [None]: json

> Access keys - credentials that give access to the permissions you have on aws 



## AWS CLI commands to manipulate S3 storage 


### List whats on aws 
```
aws s3 ls 
```

### Gives commands 

```
aws s3 help

aws s3 mb help
``` 

Gives specific commands for mb(make bucket)

### Create bucket 

```
aws s3 mb s3://tech610-ky-first-bucket
```

### List whats in bucket 
```
aws s3 ls s3://tech610-ky-first-bucket
```

### Uploading file to AWS bucket 

```
echo This is the first line in a test file > test.txt 

cat test.txt

aws s3 cp test.txt s3://tech610-ky-first-bucket

```

## making new folder to upload 
```
mkdir downloads 
cd downloads/
```

```aws s3 sync s3://<name of bucket> <path where you want the files downloaded>```

```
aws s3 sync s3://tech610-ky-first-bucket .
```

### Use history to perform command 
history 
![number of command]
enter

### ⚠️ Removing a file from bucket 

```
aws s3 rm s3://tech610-ky-first-bucket/test.txt
```

### ⚠️ Delete multiple files in bucket

```
aws s3 rm s3://tech610-ky-first-bucket --recursive
```

> ⚠️ Will delete without asking for confimation 

### ⚠️Delete a bucket with files in it

```aws s3 rb s3://tech610-ky-first-bucket``` 

^Only works if empty 


```
aws s3 rb s3://tech610-ky-first-bucket --force
```
^ correct way to do it 
> ⚠️ will delete all things IN bucket as well as the bucket itself


# What is Boto3 

Boto3 is the AWS SDK (Software Development Kit) for Python. It's a Python library that lets you interact with AWS services programmatically, instead of using the AWS CLI or clicking through the console.

## Boto3 Scripts

1. [List all the S3 buckets](list-buckets.py)
2. [Create an S3 bucket](create-bucket.py)
3. [Upload a file to the bucket](upload-bucket.py)
4. [Download file from S3 bucket ](download-file.py)
5. [Delete file from s3 bucket](delete-file.py)
6. [Delete the bucket](delete-bucket.py)

## purpose of todays tasks 

We covered two ways of manipulating S3 storage: 
- Through the AWS CLI directly on an EC2 instance
- Then through Python using boto3.

CLI is good for quick one-off commands, but boto3 is what you'd actually use to build S3 into an application, since it lets you script and automate S3 actions (list, create, upload, download, delete) as part of a larger Python program rather than typing commands one at a time.