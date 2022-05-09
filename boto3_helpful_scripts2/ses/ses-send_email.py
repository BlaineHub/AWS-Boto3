import boto3

ses = boto3.client('ses')
response = ses.send_templated_email(
    Source='blaineodriscoll91@gmail.com',
    Destination={
        'ToAddresses':['blaineodriscoll91@gmail.com']
    },
    ReplyToAddresses = ['blaineodriscoll91@gmail.com'],
    Template='CustomTemplate',
    TemplateData='{"replace":"value"}'
)

print(response)