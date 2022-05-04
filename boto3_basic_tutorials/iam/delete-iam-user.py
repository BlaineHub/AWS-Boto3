import boto3

aws=boto3.session.Session(profile_name='developer')
iam_resource=aws.resource('iam')
iam_client=aws.client('iam')

username = input('Please Enter Username to be deleted: ')
iam_user_ob = iam_resource.User(username)

pol = []   
for policy in iam_client.list_attached_user_policies(UserName=iam_user_ob.user_name)['AttachedPolicies']:
    pol.append(policy['PolicyArn'])

acckey = []
for data in iam_client.list_access_keys(UserName=username)['AccessKeyMetadata']:
    acckey.append(data['AccessKeyId'])
try: 
    for p in pol:
        iam_client.detach_user_policy(UserName=iam_user_ob.user_name,PolicyArn=p)
except Exception:
    pass
try: 
    iam_client.delete_access_key(UserName=iam_user_ob.user_name,AccessKeyId=acckey[0])
except Exception:
    pass
try:
    iam_client.delete_login_profile(UserName=iam_user_ob.user_name)
except Exception:
    pass
try:
    iam_client.delete_user(UserName=iam_user_ob.user_name)
except Exception:
    pass
print('The User {} was deleted successfully'.format(iam_user_ob.user_name))





