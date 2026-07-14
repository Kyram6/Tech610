import boto3 # import boto3 library to connect to AWS

s3 = boto3.client("s3", region_name="eu-west-1") #connect to AWS in Ireland region

bucket_name = "tech610-ky-test-boto3" # store bucket name in a variable

s3.create_bucket( # create new bucket 
    Bucket=bucket_name,
    CreateBucketConfiguration={"LocationConstraint": "eu-west-1"} # create in Ireland region
)

print(f"Created bucket: {bucket_name}") # print success message 