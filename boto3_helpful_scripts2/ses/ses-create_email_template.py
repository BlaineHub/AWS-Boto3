import boto3

ses = boto3.client('ses')
response = ses.create_template(
    Template={
        'TemplateName':'CustomTemplate',
        'SubjectPart':'Welcome to the course',
        'TextPart': 'Thanks for buying the course',
        'HtmlPart': 'Thanks for buying the course'
    }
)
print(response)