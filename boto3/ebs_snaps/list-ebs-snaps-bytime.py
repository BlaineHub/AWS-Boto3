import boto3
import datetime

aws = boto3.session.Session(profile_name='developer',region_name='us-east-1')
ec2_resource = aws.resource('ec2')
ec2_client = aws.client('ec2')
sts_client = aws.client(service_name='sts')

acc_id = sts_client.get_caller_identity()['Account']
today=datetime.datetime.now()

start_time=datetime.datetime(today.year,today.month,today.day).strftime('%Y-%m-%d')

#resource
count=0
for each in ec2_resource.snapshots.filter(OwnerIds=[acc_id]):
    print('The below snapshots were taken {}'.format(start_time))
    if start_time in each.start_time.strftime('%Y-%m-%d %H:%M:%S'):
        print(each.id, ':', each.start_time.strftime('%Y-%m-%d %H:%M:%S'))
        count +=1
if count==0:
    print('There were no snapshots taken {}'.format(start_time))


