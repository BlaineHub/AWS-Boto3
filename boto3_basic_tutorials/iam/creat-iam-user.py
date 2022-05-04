import boto3
import sys

def get_iam_client_object():
    aws=boto3.session.Session(profile_name='developer',region_name='us-east-1')
    iam_client=aws.client('iam')
    return iam_client


def main():
    iam_client=get_iam_client_object()
    iam_user_name=''
    password=''
    PolicyArn='arn:aws:iam::aws:policy/AdministratorAccess'
    try: 
        iam_client.create_user(UserName=iam_user_name)
        iam_client.create_login_profile(UserName=iam_user_name,Password=password,PasswordResetRequired=False)
        iam_client.attach_user_policy(UserName=iam_user_name,PolicyArn=PolicyArn)
        print('Success! See details below')
        print('IAM username: {} and password: {}'.format(iam_user_name,password))
    except Exception as e:
        if e.response['Error']['Code']=='EntityAlreadyExists':
            print('The Username {} already exists'.format(iam_user_name))
            sys.exit()
        else:
            print('Please correct the following Error')
            print(e)
            sys.exit()

    response = iam_client.create_access_key(UserName=iam_user_name)
    print('AccessKeyId: {}, SecretAccessKey: {}'.format(response['AccessKey']['AccessKeyId'],response['AccessKey']['SecretAccessKey']))

if __name__ == '__main__':
    main()

