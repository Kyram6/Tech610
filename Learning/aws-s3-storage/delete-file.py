import boto3

s3 = boto3.client("s3") # creates s3 client 

s3.delete_object(Bucket="tech610-ky-test-boto3", # bucket containing file 
Key="test.txt") # file to delete

print("Deleted file") #sucess message

