import boto3
from pprint import pprint

aws_console = boto3.session.Session(profile_name='developer',region_name='us-east-1')
ec2_console = aws_console.resource('ec2')
ec2_client = aws_console.client('ec2')

'''
instances_ = []
for x in ec2_console.instances.all():
    instances_.append(x.id)

waiter=ec2_client.get_waiter('instance_running')
print('Starting instances....')
ec2_console.instances.start()

waiter.wait(InstanceIds=instances_)
print('All instances are running now')
'''

np_sers_id=[]
f1={'Name':'tag:Name','Values':['non-prod']}
'''
for x in ec2_console.instances.filter(Filters=[f1]):
    np_sers_id.append(x.id)
print(np_sers_id)
print('----------------')
'''
for x in ec2_client.describe_instances(Filters=[f1])['Reservations']:
    for y in x['Instances']:
        np_sers_id.append(y['InstanceId'])
print(np_sers_id)


ec2_client.start_instances(InstanceIds=np_sers_id)
print('Starting np instances....')
waiter=ec2_client.get_waiter('instance_running')
waiter.wait(InstanceIds=np_sers_id)
print('All np instances are running now')





