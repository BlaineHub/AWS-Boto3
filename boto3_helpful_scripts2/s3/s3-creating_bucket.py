import boto3


bucket = boto3.resource('s3')
response = bucket.create_bucket(
    Bucket = 'Test',
    ACL= 'public'
)
print(response)

'''
bucket = boto3.client('s3')
response = bucket.create_bucket(
    Bucket = 'blaine-test2',
    ACL = 'public-read-write'
)
print(response)
'''
