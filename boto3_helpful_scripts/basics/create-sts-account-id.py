import boto3

aws_console = boto3.session.Session(profile_name='developer')
sts_console = aws_console.client(service_name='sts',region_name='us-east-1')

print(sts_console.get_caller_identity()['Account'])

print('Test Commit')