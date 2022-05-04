import boto3

BUCKET_NAME = 'blaine-s3-demo'

s3_client = boto3.client('s3')

def upload_files(file_name,bucket,object_name=None,args=None):
    if object_name is None:
        object_name = file_name

    s3_client.upload_file(file_name,bucket,object_name, ExtraArgs=args)
    print(f'{file_name} has been uploaded to {bucket} bucket')

upload_files('download.png',BUCKET_NAME)

'''
#Method2 Resource & Meta
s3_resource = boto3.resource('s3')
def upload_files(file_name,bucket,object_name=None,args=None):
    if object_name is None:
        object_name = file_name

    s3_resource.meta.client.upload_file(file_name,bucket,object_name, ExtraArgs=args)
    print(f'{file_name} has been uploaded to {bucket} bucket')

upload_files('moviedata.json',BUCKET_NAME)
'''