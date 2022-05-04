import boto3

aws=boto3.session.Session(profile_name='developer',region_name='us-east-1')
iam_client=aws.client('iam')
with open('./csv/iam_users.csv','r') as file:
    all_users = file.readlines()

all_users_split = []
for user in all_users:
    all_users_split.append(user.split(','))
all_users_split = all_users_split[1:]


for user in all_users_split:
    iam_user_name=user[1]
    password='Blaine91'
    PolicyArn=user[4].strip('\n')
    iam_client.create_user(UserName=iam_user_name)
    iam_client.attach_user_policy(UserName=iam_user_name,PolicyArn=PolicyArn)
    if user[2] == 'Yes':
        response = iam_client.create_access_key(UserName=iam_user_name)
    else:
        pass
    if user[3]=='Yes':
        iam_client.create_login_profile(UserName=iam_user_name,Password=password,PasswordResetRequired=False)
    else:
        pass
    print('IAM username: {} and password: {}'.format(iam_user_name,password))
    if user[2] == 'Yes':
        print('AccessKeyId: {}, SecretAccessKey: {}'.format(response['AccessKey']['AccessKeyId'],response['AccessKey']['SecretAccessKey']))
    else:
        pass
    print('----------------')