import boto3

def create_movie_table(dynamodb=None):
    db = boto3.resource('dynamodb')
    table = db.create_table(
        TableName='Movies',
        KeySchema=[
            {
                'AttributeName':'year',
                'KeyType': 'HASH'
            },
            {
                'AttributeName':'title',
                'KeyType': 'RANGE'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName':'year',
                'AttributeType':'N'
            },
             {
                'AttributeName':'title',
                'AttributeType':'S'
            }
        ],
        ProvisionedThroughput = {
            'ReadCapacityUnits':5,
            'WriteCapacityUnits':5
        }
    )
    return table

if __name__ == '__main__':
    movie_table = create_movie_table()
    print("Table Status:", movie_table.table_status)
