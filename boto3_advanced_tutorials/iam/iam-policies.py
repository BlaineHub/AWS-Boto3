import boto3, json

#custom admin policy
def create_policy():
    iam = boto3.client('iam')
    user_policy = {
        "Version":"2012-10-17",
        "Statement":[
        {
            "Effect":"Allow",
            "Action":"*",
            "Resource":"*"
        }
        ]
    }

    response = iam.create_policy(
        PolicyName = 'pyFullAccess',
        PolicyDocument=json.dumps(user_policy)
    )
    print(response)

def list_policies():
    iam=boto3.client('iam')
    paginator = iam.get_paginator('list_policies')
    
    for page in paginator.paginate(Scope='Local'):
        for policy in page['Policies']:
            print(policy['PolicyName'])


def add_policies(policy_arn, username):
    iam=boto3.client('iam')

    response = iam.attach_user_policy(
        UserName = username,
        PolicyArn = policy_arn
    )
    print(response)



def detach_policies(policy_arn, username):
    iam=boto3.client('iam')

    response = iam.detach_user_policy(
        UserName = username,
        PolicyArn = policy_arn
    )
    print(response)

