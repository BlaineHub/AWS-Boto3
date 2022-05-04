import boto3

#Client (all services available, returns dictionary with keys)
aws_mag_con = boto3.session.Session(profile_name='developer')


iam_client=aws_mag_con.client(service_name='iam')
ec2_client=aws_mag_con.client(service_name='ec2',region_name='us-east-1')
s3_client=aws_mag_con.client(service_name='s3')


res = iam_client.list_users()['Users']
for iam_user in res:
    print(iam_user['UserName'])

print('-----------------------------')

res2 = ec2_client.describe_instances()['Reservations']
for ec2_all in res2:
    for ec2 in ec2_all['Instances']:
        print(ec2['InstanceId'])

print('-----------------------------')

res3 = s3_client.list_buckets()['Buckets']
for s3 in res3:
    print(s3['Name'])


   



