import boto3
aws = boto3.session.Session(profile_name='developer')


ec2_con=aws.client(service_name='ec2')

res2 = ec2_con.describe_instances()['Reservations']
for ec2_all in res2:
    for ec2 in ec2_all['Instances']:
        print(ec2['InstanceId'])

print('-----------------------------')

ec2_paginator = ec2_con.get_paginator('describe_instances')
for each_page in ec2_paginator.paginate():
    for ec2_all in each_page['Reservations']:
        for ec2 in ec2_all['Instances']:
            print(ec2['InstanceId'])