import boto3
from pprint import pprint

cf_client = boto3.client('cloudformation')
response = cf_client.delete_stack(
    StackName='dynamostack'
)
print(response)