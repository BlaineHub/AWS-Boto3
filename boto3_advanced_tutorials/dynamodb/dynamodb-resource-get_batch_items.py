import boto3
from pprint import pprint

db = boto3.resource('dynamodb')
table = db.Table('employees')
'''
response = table.get_item(
    Key = {
        'emp_id': "2"
    }
)
print(response['Item']['name'])
'''
response = db.batch_get_item(
    RequestItems={
        'employees':{
            'Keys':[
                {
                    'emp_id':'2'
                },
                {
                    'emp_id':'3'
                },
                {
                    'emp_id':'4'
                }
            ]
        }
    }
)

pprint(response['Responses'])