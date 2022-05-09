import boto3
import sys


aws_console=boto3.session.Session(profile_name='developer')
ec2_resource=aws_console.resource(service_name='ec2',region_name='us-east-1')


while True:
    print('This Script performs the following actions on ec2 isntance')
    print('''
    1. start
    2. stop
    3. terminate
    4. exit
    ''')
    opt=int(input('Enter your option: '))
    if opt==1:
        instance_id=input('Enter your ec2 instance id: ')
        instance_object = ec2_resource.Instance(instance_id)
        print('starting ec2 instance')
        instance_object.start()
    elif opt==2:
        instance_id=input('Enter your ec2 instance id: ')
        instance_object = ec2_resource.Instance(instance_id)
        print('stoping ec2 instance')
        instance_object.stop()
    elif opt==3:
        instance_id=input('Enter your ec2 instance id: ')
        instance_object = ec2_resource.Instance(instance_id)
        print('terminating ec2 instance')
        instance_object.terminate()
    elif opt==4:
        print('exiting script')
        sys.exit()
    else:
        instance_id=input('Enter your ec2 instance id: ')
        print('option not valid')

