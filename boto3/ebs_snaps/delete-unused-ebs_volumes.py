import boto3
from pprint import pprint

aws = boto3.session.Session(profile_name='developer',region_name='us-east-1')
ec2_resource = aws.resource('ec2')
ec2_client = aws.client('ec2')

#Resource
f_ebs_unused={'Name':'status','Values':['available']}
for each_volume in ec2_resource.volumes.all().filter(Filters=[f_ebs_unused]):
        print(each_volume.id,each_volume.state,each_volume.tags)
        print('Deleting unused volumes.....')
        each_volume.delete()
print('Deleted all unused volumes')


#Client
f_ebs_unused={'Name':'status','Values':['available']}
for each_volume in ec2_client.describe_volumes()['Volumes']:
    if each_volume['State'] == 'available':
        print('Deleting' ,each_volume['VolumeId'])
        ec2_client.delete_volume(VolumeId=each_volume['VolumeId'])

