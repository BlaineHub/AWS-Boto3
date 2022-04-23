import boto3
from pprint import pprint

aws_console=boto3.session.Session(profile_name='developer')
ec2_client = aws_console.client('ec2',region_name='us-east-1')

'''
response = ec2_client.describe_instances()['Reservations']
for x in response:
    for y in x['Instances']:
        print("the image id is {}\n,The instance id is {}\n the instance launch time is {}".format(y['ImageId'],y['InstanceId'],y['LaunchTime'].strftime('%Y-%m-%d')))
'''

response = ec2_client.describe_volumes()['Volumes']
for x in response:
    print('the volume id is {}\n the AvailabilityZone is {}\n the volume type is {}'.format(
             x['VolumeId'],x['AvailabilityZone'],x['VolumeType']))