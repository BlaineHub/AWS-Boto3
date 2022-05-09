import boto3
from pprint import pprint

rds_client = boto3.client('rds')
response = rds_client.create_db_instance(
    DBName='blogdb',
    DBInstanceIdentifier='blogdb',
    AllocatedStorage=20,
    DBInstanceClass='db.t2.micro',
    Engine='MySQL',
    MasterUsername='admin',
    MasterUserPassword='12345678',
    Port=3306,
    EngineVersion='8.0.27',
    PubliclyAccessible=True,
    StorageType='gp2'
)

pprint(response)