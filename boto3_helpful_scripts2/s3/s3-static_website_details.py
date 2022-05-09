import boto3
from pprint import pprint

client = boto3.client('s3')

response = client.get_bucket_website(
    Bucket='blaine-web-911'
)

pprint(response)