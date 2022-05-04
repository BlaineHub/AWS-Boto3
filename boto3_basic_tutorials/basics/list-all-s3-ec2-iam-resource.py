import boto3

#Resource (limited services available, returns Object with dot)
aws_console=boto3.session.Session(profile_name='developer')

iam_res = aws_console.resource('iam')
ec2_res = aws_console.resource('ec2',region_name='us-east-1')
s3_res = aws_console.resource('s3')

for iam_user in iam_res.users.limit(1):
    print(iam_user.name)

print('-------------------------')

for s3 in s3_res.buckets.all():
    print(s3.name)

print('--------------------------')

for ec2 in ec2_res.instances.all():
    print(ec2.id)
   


