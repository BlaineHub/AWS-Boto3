import boto3

def get_instances():
    ec2_client = boto3.client('ec2')
    reservations = ec2_client.describe_instances().get('Reservations')
    
    for res in reservations:
        for instance in res['Instances']:
            print(instance['InstanceId'])
            print(instance['InstanceType'])
            print(instance['PublicIpAddress'])
            print(instance['PrivateIpAddress'])
            print('-----------------------')

get_instances()




