import boto3
from pprint import pprint

aws_console=boto3.session.Session(profile_name='developer')
ec2_client = aws_console.client('ec2',region_name='us-east-1')


ls = []
response = ec2_client.describe_instances()['Reservations']
for x in response:
    for y in x['Instances']:
        ls.append(y['InstanceId'])

ec2_client.terminate_instances(InstanceIds=ls)



