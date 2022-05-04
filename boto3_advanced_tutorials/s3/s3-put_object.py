import boto3

client = boto3.client('s3')

with open('download.png','rb') as f:
    data = f.read()

response = client.put_object(
    ACL="public-read",
    Bucket = "blaines-bucket",
    Body=data,
    Key='download.png'
)
print(response)