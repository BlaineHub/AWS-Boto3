import boto3


db = boto3.resource('dynamodb')
table = db.Table('employees')

table.put_item(
    Item = {
        'emp_id':"2",
        'name':"test",
        'age':24
    }
)


db = boto3.client('dynamodb')
response = db.put_item(
    TableName='employees',
    Item = {
        'emp_id':{
            'S':'3'
        },
        'name':{
            'S':'newname'
        },
        'age':{
            'S':'20'
        }
    }
)
