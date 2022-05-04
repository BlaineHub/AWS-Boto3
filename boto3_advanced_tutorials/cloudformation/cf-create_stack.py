import boto3

cf_client = boto3.client('cloudformation')

with open('boto3_advanced/cloudformation/Dynamodb.yml','r') as f:
    template = f.read()
params = [

   { 
       'ParamaterKey':'HashKeyElementName',
       'ParameterValue':'EmployeeId'
   }
]

response = cf_client.create_stack(
    StackName='dynamostack',
    TemplateBody=template
)
print(response)