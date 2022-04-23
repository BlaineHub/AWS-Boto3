import boto3
from pprint import pprint
aws_console = boto3.session.Session(profile_name='developer')
ec2_res = aws_console.resource('ec2',region_name='us-east-1')

y = ec2_res.meta.client.describe_regions()['Regions']
for x in y:
    print(x['RegionName'])