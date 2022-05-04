import boto3

client = boto3.client('s3')

response = client.delete_bucket_website(
    Bucket = 'blaine-web-911'
)

print(response)