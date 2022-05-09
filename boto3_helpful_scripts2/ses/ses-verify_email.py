import boto3

ses = boto3.client('ses')
response = ses.verify_email_address(
    EmailAddress='blaineodriscoll91@gmail.com'
)
print(response)