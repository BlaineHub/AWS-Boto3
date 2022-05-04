import boto3
from pprint import pprint

ec2_client = boto3.client('ec2')
response = ec2_client.authorize_security_group_ingress(
    GroupId='sg-0765294b59ac1344f',
    IpPermissions= [
        {
            'IpProtocol':'tcp',
            'FromPort':80,
            'ToPort':80,
            'IpRanges':[{'CidrIp':'0.0.0.0/0'}]
        },
        {
            'IpProtocol':'tcp',
            'FromPort':22,
            'ToPort':22,
            'IpRanges':[{'CidrIp':'0.0.0.0/0'}]
        }
    ]
)

print(response)