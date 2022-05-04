import boto3
from pprint import pprint
from botocore.exceptions import ClientError

def delete_movie(title,year,dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('Movies')
    try:
        response=table.delete_item(Key={'year':year,'title':title})
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response

if __name__=="__main__":
    response = delete_movie('Insidious: Chapter 2',2013)
    pprint(response)
    
   