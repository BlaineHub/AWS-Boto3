import boto3

def create_group(group_name):
    iam = boto3.client('iam')
    iam.create_group(GroupName=group_name)

def attach_policy(policy_arn, group_name):
    iam = boto3.client('iam')
    response = iam.attach_group_policy(
        GroupName=group_name,
        PolicyArn=policy_arn
    )

def add_user(username,group_name):
    iam = boto3.client('iam')

    response = iam.add_user_to_group(
        UserName = username,
        GroupName = group_name
    )

    print(response)

def detach_grp_policy(user_group, arn):
    iam = boto3.client('iam')
    response = iam.detach_group_policy(
        GroupName=user_group,
        PolicyArn=arn
    )
    print(response)






