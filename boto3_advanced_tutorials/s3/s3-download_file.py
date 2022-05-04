import boto3

BUCKET_NAME = 'blaine-s3-demo'
file = 'moviedata.json'

s3_resource = boto3.resource('s3')
s3_object = s3_resource.Object(BUCKET_NAME,file)
s3_object.download_file('download.json')
print(f'{file} has been downloaded')