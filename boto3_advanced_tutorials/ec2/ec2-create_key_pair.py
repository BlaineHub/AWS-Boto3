import boto3
from pprint import pprint

ec2_client = boto3.client('ec2')
response = ec2_client.create_key_pair(
    KeyName = 'mykey',
    KeyType = 'rsa'
)
pprint(response)

file = open('mykey.pem','w')
file.write(response['MyKeyMaterial'])
file.close