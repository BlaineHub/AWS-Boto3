import boto3
import csv

from flask_login import user_accessed

aws=boto3.session.Session(profile_name='developer',region_name='us-east-1')
iam_client=aws.client('iam')
iam_resource=aws.resource('iam')

count=1
csv_ob=open('./csv/iam_details.csv','w',newline='')
csv_w=csv.writer(csv_ob)
csv_w.writerow(['S_NO','IAM_USER_NAME','IAM_USER_ID','ARN','CREATED DATE','POLICIES','GROUPS'])

for user in iam_resource.users.all():
    ls=[]
    ls.append(user.user_name)
    ls.append(user.user_id)
    ls.append(user.arn)
    ls.append(user.create_date.strftime('%Y-%m-%d'))
    if len(iam_client.list_groups_for_user(UserName=user.user_name)['Groups'])==0:
        ls.append('None')
    else:
        for item in iam_client.list_groups_for_user(UserName=user.user_name)['Groups']:
            ls.append(item['GroupName'])
    if len(iam_client.list_attached_user_policies(UserName=user.user_name)['AttachedPolicies'])==0:
        ls.append('None')
    else:
        for policy in iam_client.list_attached_user_policies(UserName=user.user_name)['AttachedPolicies']:
            ls.append(policy['PolicyArn'])
    csv_w.writerow([count,ls[1],ls[0],ls[3],ls[2],ls[4],ls[5]])
    count+=1
csv_ob.close()

