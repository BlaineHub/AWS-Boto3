import boto3

db = boto3.client('dynamodb')
response=db.delete_table(TableName='Employee')

print(response)
    