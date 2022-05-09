import boto3

BUCKET_NAME = 'blaine-bucket'
s3 = boto3.resource('s3')
s3_bucket = s3.Bucket(BUCKET_NAME)

def clean_up():
    for obj in s3_bucket.objects.all():
        obj.delete()
    
    for obj_ver in s3_bucket.object_versions.all():
        obj_ver.delete()
    
    print('{} is now empty'.format(BUCKET_NAME))

clean_up()
s3_bucket.delete()

print('{} has been deleted'.format(BUCKET_NAME))


