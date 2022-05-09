import boto3
from pprint import pprint
from botocore.exceptions import ClientError
from decimal import Decimal

def update_movie(title,year,rating,plot,dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('Movies')
    response = table.update_item(
        Key={
            'year': year,
            'title': title,
        },
        UpdateExpression="set info.rating=:r, info.plot=:p",
        ExpressionAttributeValues = {
            ':r':Decimal(rating),
            ':p':plot,
        },
        ReturnValues='UPDATED_NEW'
    )
    return response


if __name__ == '__main__':
    update_response = update_movie(
        "Insidious: Chapter 2", 2013, "3.1","This is updated"
    )

    pprint(update_response)

