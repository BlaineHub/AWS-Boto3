import boto3
from pprint import pprint


ses = boto3.client('ses')

def get_template():
    response = ses.get_template(
    TemplateName='CustomTemplate'
    )
    pprint(response['Template'])

def list_template():
    response = ses.list_templates()
    print(response['TemplatesMetadata'])

list_template()