import boto3
from pprint import pprint

aws_console=boto3.session.Session(profile_name='developer')
ec2_client = aws_console.client('ec2',region_name='us-east-1')

response = ec2_client.describe_instances()['Reservations']
for ec2_ob in response:
    for ec2 in ec2_ob['Instances']:
        print("the image id is {}\n,The instance id is {}\n the instance launch time is {}".format(ec2['ImageId'],ec2['InstanceId'],ec2['LaunchTime'].strftime('%Y-%m-%d')))
print('--------------------')

response = ec2_client.describe_volumes()['Volumes']
for ec2 in response:
    print('the volume id is {}\n the AvailabilityZone is {}\n the volume type is {}'.format(
             ec2['VolumeId'],ec2['AvailabilityZone'],ec2['VolumeType']))