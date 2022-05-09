import boto3
from pprint import pprint

ec2_client = boto3.client('ec2')
response = ec2_client.create_security_group(
    Description = 'This is desc',
    GroupName = 'pygroup',
    VpcId = 'vpc-0964780bc2b65a0e8'
)
pprint(response)