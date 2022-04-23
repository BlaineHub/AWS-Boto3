import boto3

#Client (all services available, returns dictionary with keys)
aws_mag_con = boto3.session.Session(profile_name='developer')


iam_client=aws_mag_con.client(service_name='iam')
ec2_client=aws_mag_con.client(service_name='ec2',region_name='us-east-1')
s3_client=aws_mag_con.client(service_name='s3')


response = iam_client.list_users()['Users']
for x in response:
    print(x['UserName'])

response2 = ec2_client.describe_instances()['Reservations']
for x in response2:
    for y in x['Instances']:
        print(y['InstanceId'])

response3 = s3_client.list_buckets()['Buckets']
for x in response3:
    print(x['Name'])


   



