import boto3

s3 = boto3.client("s3") #creayes s3 client 

s3.download_file("tech610-ky-test-boto3", # bucket to downlod from
"test.txt", # file stored in s3
"downloaded-test.txt") # where to save it locally

print("Downloaded test.txt") 


