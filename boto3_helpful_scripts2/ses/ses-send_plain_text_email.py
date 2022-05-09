import boto3

ses = boto3.client('ses')
CHARSET='UTF-8'

response = ses.send_email(
    Destination={
        'ToAddresses':['blaineodriscoll91@gmail.com']
    },
    Message={
        'Body':{
            'Text':{
                'Charset':CHARSET,
                'Data':'Thanks for buying the course'
            }
        },
        'Subject':{
                'Charset':CHARSET,
                'Data':'AWS course with python & Boto3'
        }
    },
    Source = 'blaineodriscoll91@gmail.com'
)

print(response)