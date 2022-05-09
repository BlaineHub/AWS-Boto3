import boto3

ses = boto3.client('ses')
response = ses.list_identities(
    IdentityType = 'EmailAddress'
)

for email in response['Identities']:
    print(email)