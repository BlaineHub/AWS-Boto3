import boto3

aws=boto3.session.Session(profile_name='developer',region_name='us-east-1')
iam_resource=aws.resource('iam')

for group in iam_resource.groups.all():
    print(group.name)


