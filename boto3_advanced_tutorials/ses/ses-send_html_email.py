import boto3

ses = boto3.client('ses')
CHARSET='UTF-8'
html_email_content="""
        <html>
            <head></head>
            <h1 style='text_align:center'>AWS</h1>
            <p style='color:red'>Welcome to New Town</p>
        </html>
"""
response = ses.send_email(
    Destination={
        'ToAddresses':['blaineodriscoll91@gmail.com']
    },
    Message={
        'Body':{
            'Html':{
                'Charset':CHARSET,
                'Data':html_email_content
            }
        },
        'Subject':{
                'Charset':CHARSET,
                'Data':'AWS Html Test'
        }
    },
    Source = 'blaineodriscoll91@gmail.com'
)

print(response)