from pprint import pprint
import boto3

DBNAME = 'blogdb'
rds_client = boto3.client('rds')
response = rds_client.describe_db_instances(
    DBInstanceIdentifier = DBNAME
)

print(f'The status of {DBNAME} is: ',response['DBInstances'][0]['DBInstanceStatus'])
print('----------------------------------------')
try: 
    for item in response['DBInstances'][0]['Endpoint'].items():
        print(item[0], ':', item[1])
except:
    print(f'Endpoint setup still in progess...')

