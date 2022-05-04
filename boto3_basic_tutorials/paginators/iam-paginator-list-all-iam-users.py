import boto3
aws = boto3.session.Session(profile_name='developer')


iam_con=aws.client(service_name='iam')

res = iam_con.list_users()['Users']
for iam_user in res:
    print(iam_user['UserName'])

print('-----------------------------')

iam_paginator = iam_con.get_paginator('list_users')
for each_page in iam_paginator.paginate():
    for iam_user in each_page['Users']:
        print(iam_user['UserName'])
