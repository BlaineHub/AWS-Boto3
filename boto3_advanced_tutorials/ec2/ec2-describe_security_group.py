import boto3
from pprint import pprint

ec2_client = boto3.client('ec2')
response = ec2_client.describe_security_groups()
for res in response['SecurityGroups']:
    print(res['GroupName'])
    print(res['GroupId'])
    print('-------------')
