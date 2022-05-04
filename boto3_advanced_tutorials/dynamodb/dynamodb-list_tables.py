import boto3

db = boto3.client('dynamodb')
response = db.list_tables()
#print(response['TableNames'])

response = db.update_table(
    TableName='employees',
    BillingMode='PROVISIONED',
    provisionedThroughput={
        'ReadCapacityUnits':5,
        'WriteCapacityUnits':5,
    }
    )
#print(response)