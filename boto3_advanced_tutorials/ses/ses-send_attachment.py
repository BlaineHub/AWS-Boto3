from functools import partial
import boto3
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


CHARSET='UTF-8'
msg = MIMEMultipart()

msg['Subject']='This is a boto3 test'
msg['From']='blaineodriscoll91@gmail.com'
msg['To']='blaineodriscoll91@gmail.com'

body= MIMEText('Thanks for being cool')
msg.attach(body)

filename = 'aws.png'
with open(filename,'rb') as f:
    part = MIMEApplication(f.read())
    part.add_header('Content-Disposition',
                    'attachment',
                    filename=filename)
msg.attach(part)

ses = boto3.client('ses')
response = ses.send_raw_email(
    Source='blaineodriscoll91@gmail.com',
    Destinations=['blaineodriscoll91@gmail.com'],
    RawMessage={"Data":msg.as_string()}
)




  