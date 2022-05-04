import boto3

ec2_resource = boto3.resource('ec2')
response = ec2_resource.create_instances(
    ImageId = 'ami-0022f774911c1d690',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    KeyName='',
    SecurityGroups = [
        'pygroup'
    ]
)
print(response)

