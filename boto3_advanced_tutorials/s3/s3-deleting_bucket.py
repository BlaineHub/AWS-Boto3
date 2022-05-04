import boto3

client = boto3.client('s3')
bucket_name = 'blaine-web-911'
client.delete_bucket(Bucket=bucket_name)
print('{} deleted'.format(bucket_name))

'''
resource = boto3.resource('s3')
bucket_name = ''
resource.Bucket(bucket_name).delete()
print(f'{bucket_name} Bucket Deleted')
'''
