import boto3
import time

aws_console = boto3.session.Session(profile_name='developer',region_name='us-east-1')
ec2_resource = aws_console.resource('ec2')
ec2_client = aws_console.client('ec2')

my_inst_ob=ec2_resource.Instance('i-0c6d2ef6115ef773f')
print('starting given instance....')
my_inst_ob.start()

while True:
    my_inst_ob = ec2_resource.Instance('i-0c6d2ef6115ef773f')
    print('the current status is {}'.format(my_inst_ob.state['Name']))
    if my_inst_ob.state['Name']=='running':
        break
    print('Waiting to get running status...')
    time.sleep(5)
print('Now your instance is running')


