import boto3
aws=boto3.session.Session(profile_name='developer')
s3_con_re=aws.resource('s3')
s3_con_cl=aws.client('s3')

bucket_list=[]
for bucket in s3_con_re.buckets.all():
    bucket_list.append(bucket.name)
bucket_name = bucket_list[0]

class BucketObjects:
    def __init__(self,bucket_name):
        self.bucket_name = bucket_name
    
    def objects(self):
        print('Returned using resource, The objects in {} are: '.format(self.bucket_name))
        bucket_object=s3_con_re.Bucket(self.bucket_name)
        cnt=1
        for each_obj in bucket_object.objects.all():
            print(cnt,each_obj.key)
            cnt +=1
        print('------------------------')

my_bucket_re = BucketObjects(bucket_name)
my_bucket_re.objects()


class BucketPaginator:
    def __init__(self,bucket_name):
        self.bucket_name = bucket_name

    def objects(self):
        print('Returned using client & pagainator, the objects in {} are: '.format(self.bucket_name))
        cnt =1
        paginator = s3_con_cl.get_paginator('list_objects')
        for each_page in paginator.paginate(Bucket=self.bucket_name):
            for object in each_page['Contents']:
                print(cnt, object['Key'])
                cnt +=1   
        print('-------------------------')

my_bucket_cli = BucketPaginator(bucket_name)
my_bucket_cli.objects()





