import boto3

ec2_client = boto3.client('ec2')
response = ec2_client.delete_security_group(
    GroupId = 'sg-0765294b59ac1344f'
)
print(response)
