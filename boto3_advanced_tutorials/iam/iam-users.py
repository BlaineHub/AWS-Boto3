import boto3
import json

def create_user(username):
    iam = boto3.client('iam')
    response = iam.create_user(UserName=username)
    print(response)

def all_users():
    iam = boto3.client('iam')
    paginator = iam.get_paginator('list_users')
    for response in paginator.paginate():
        for user in response['Users']:
            print(user['UserName'], user['Arn'])

def update_user(old_username, new_username):
    iam = boto3.client('iam')
    response = iam.update_user(
        UserName = old_username,
        NewUserName=new_username
    )

def create_access_key(username):
    iam = boto3.client('iam')
    response = iam.create_access_key(
        UserNaem=username
    )
    print(response)

def update_access_key(username,acc_id):
    iam = boto3.client('iam')
    iam.update_access_key(
    UserName= username,
    AccessKeyId = acc_id,
    Status='Inactive'  
    )

def update_login_access(username):
    iam = boto3.client('iam')
    login_profile = iam.create_login_profile(
        Password = '12345678',
        PasswordResetRequied = False,
        Username = username
    )
    print(login_profile)

def delete_user(username):
    iam = boto3.client('iam')
    response = iam.delete_user(
        UserName=username
    )
    print(response)
#must detach all policies

def delete_user_group(username, groupname):
    iam = boto3.resource('iam')
    group=iam.Group(groupname)
    response = group.remove_user(
        UserName=username
    )
    print(response)


delete_user_group('BlaineDev','S3admins')










