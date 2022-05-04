import boto3


db = boto3.client('dynamodb')
'''
response = db.create_backup(
    TableName='Articles',
    BackupName='ArticlesBackUp'
)
print(response)
'''

response = db.delete_backup(
    BackupArn = 'arn:aws:dynamodb:us-east-1:563281842439:table/Articles/backup/01651391257479-3af2caeb'
)
print(response)