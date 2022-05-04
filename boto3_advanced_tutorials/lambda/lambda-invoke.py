import boto3
import json

lambda_client = boto3.client('lambda')
test_event = dict()

response = lambda_client.invoke(
    FunctionName='helloWorldLambda',
    Payload = json.dumps(test_event)
)

print(response['Payload'])
print(response['Payload'].read().decode('utf-8').split('\\')[1])