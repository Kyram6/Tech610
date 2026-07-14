import boto3

s3 = boto3.client("s3") #creates S3 client 

s3.delete_bucket(Bucket="tech610-ky-test-boto3") #bucket_name # delete the bucket 

print("Deleted bucket")
