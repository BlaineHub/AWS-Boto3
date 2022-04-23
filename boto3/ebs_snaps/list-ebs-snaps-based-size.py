import boto3

aws = boto3.session.Session(profile_name='developer',region_name='us-east-1')
ec2_resource = aws.resource('ec2')
ec2_client = aws.client('ec2')
sts_client = aws.client(service_name='sts')

acc_id = sts_client.get_caller_identity()['Account']

#resource
f_size={'Name':'volume-size','Values':['8']}
for each in ec2_resource.snapshots.all().filter(OwnerIds=[acc_id],Filters=[f_size]):
    print(each.id)
