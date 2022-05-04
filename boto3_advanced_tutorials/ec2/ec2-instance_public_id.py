import boto3

def get_ip(instance_id):
    ec2_client = boto3.client('ec2')
    response = ec2_client.describe_instances(InstanceIds=[instance_id]).get('Reservations')
    for res in response:
        for instance in res['Instances']:
            print(instance.get('PublicIpAddress'))

get_ip('')

