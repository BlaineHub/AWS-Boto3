import boto3
aws=boto3.session.Session(profile_name='developer')
s3_con_re=aws.resource('s3')
s3_con_cl=aws.client('s3')

print('List of buckets using resource')
for bucket in s3_con_re.buckets.all():
    print(bucket.name)
print('--------------------')

print('List of buckets using client')
for bucket in s3_con_cl.list_buckets()['Buckets']:
    print(bucket['Name'])
print('--------------------')


print('This query was ran by: ',end='')
sts_console = aws.client(service_name='sts',region_name='us-east-1')
print(sts_console.get_caller_identity()['Arn'].split('/')[1])


