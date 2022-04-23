import boto3

aws = boto3.session.Session(profile_name='developer',region_name='us-east-1')
ec2_resource = aws.resource('ec2')
ec2_client = aws.client('ec2')
sts_client = aws.client(service_name='sts')

acc_id = sts_client.get_caller_identity()['Account']

#Client
for each in ec2_client.describe_snapshots(OwnerIds=[acc_id])['Snapshots']:
    print(each['SnapshotId'])

#Resource 
for each in ec2_resource.snapshots.filter(OwnerIds=[acc_id]):
    print(each.delete())

