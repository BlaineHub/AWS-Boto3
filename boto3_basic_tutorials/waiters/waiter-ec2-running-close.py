import boto3
import time

aws_console = boto3.session.Session(profile_name='developer',region_name='us-east-1')
ec2_resource = aws_console.resource('ec2')
ec2_client = aws_console.client('ec2')

'''
my_inst_ob=ec2_resource.Instance('i-0c6d2ef6115ef773f')
print('starting given instance....')
my_inst_ob.start()
my_inst_ob.wait_until_running() #Resource waits for 200s, then error. (40x5)
print('Now your instance is running')
'''

my_inst_ob=ec2_resource.Instance('i-0c6d2ef6115ef773f')
print('starting given instance....')
my_inst_ob.start()
waiter=ec2_client.get_waiter('instance_running')   #(40x15 nearly 10mins)
waiter.wait(InstanceIds=['i-0c6d2ef6115ef773f'])
print('Your instance is now running')



