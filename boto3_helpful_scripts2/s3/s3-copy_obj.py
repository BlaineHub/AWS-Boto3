import boto3


s3 = boto3.resource('s3')

copy_source = {
    'Bucket':'blaine-s3-demo',
    'Key':'moviedata.json'
}

s3.meta.client.copy(copy_source,'blaine-test2','copied.json')