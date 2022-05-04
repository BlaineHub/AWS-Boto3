import boto3


db = boto3.resource('dynamodb')
table = db.Table('employees')

with table.batch_writer() as batch:
    batch.put_item(
        Item = {
            'emp_id':"3",
            'name':"test",
            'age':24
            }
        )
    batch.put_item(
        Item = {
            'emp_id':"4",
            'name':"test",
            'age':24
            }
        )