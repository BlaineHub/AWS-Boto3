import boto3
from pprint import pprint

db = boto3.resource('dynamodb')
table = db.Table('employees')

response = table.scan()
data = response['Items']
pprint(data)



