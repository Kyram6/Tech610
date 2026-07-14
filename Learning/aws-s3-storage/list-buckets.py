import boto3

s3 = boto3.client("s3") #creates s3 client = "create a connection to amazon s3"

response = s3.list_buckets() # list every bucket in your account. The result comes back as a dict, stored in response

for bucket in response["Buckets"]:
    print(bucket["Name"])