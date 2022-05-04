from pprint import pprint
import boto3

rds_client = boto3.client('rds')
response = rds_client.delete_db_instance(
    DBInstanceIdentifier = 'mariadb',
    SkipFinalSnapshot=False,
    FinalDBSnapshotIdentifier = 'mariadb-final-snapshot',
    DeleteAutomatedBackups = True
)
pprint(response)

