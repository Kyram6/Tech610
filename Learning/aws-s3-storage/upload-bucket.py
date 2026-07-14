import boto3

s3 = boto3.client("s3")

s3.upload_file("test.txt", # file on computer
    "tech610-ky-test-boto3", # s3 bucket 
    "test.txt") # name in s3

print("Uploaded test.txt")