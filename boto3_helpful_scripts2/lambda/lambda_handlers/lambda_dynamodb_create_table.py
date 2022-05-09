import boto3

def lambda_handler(event,context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.create_table(
        TableName = 'Users',
        KeySchema=[
            {
            'AttributeName':'id',
            'KeyType':'HASH'
            }
        ],
        AttributeDefinitions=[
            {
            'AttributeName':'id',
            'KeyType':'N'

            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits':3,
            'WriteCapacityUnits':3
        }
        )

    print('Table Status: ',table.table_status)