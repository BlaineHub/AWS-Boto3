import boto3

BUCKET_NAME = 'blaine-test2'

s3_resource = boto3.resource('s3')
s3_bucket = s3_resource.Bucket(BUCKET_NAME)

print("Listing all files in {}".format(BUCKET_NAME))

for file in s3_bucket.objects.all():
    print(file.key)

print('---------------------------')

'''
print('Listing all files filtered by **file**')
for file in s3_bucket.objects.filter(Prefix='file'):
    print(file.key)

print('---------------------------')
obj_summary = s3_resource.ObjectSummary(BUCKET_NAME,'moviedata.json')
print(obj_summary)
'''