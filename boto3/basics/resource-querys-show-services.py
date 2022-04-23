import boto3

#Resource (limited services available, returns Object with dot)
aws_console=boto3.session.Session(profile_name='developer')

iam_resource = aws_console.resource('iam')
ec2_resource = aws_console.resource('ec2',region_name='us-east-1')
s3_resource = aws_console.resource('s3')

#for x in iam_resource.users.limit(1):
    #print(x.name)

#for x in s3_resource.buckets.all():
    #print(x.name)

for x in ec2_resource.instances.all():
    print(x.id)
   


