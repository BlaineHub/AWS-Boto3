import boto3
aws_mag_con=boto3.session.Session(profile_name='developer')
s3_con=aws_mag_con.resource('s3')

for bucket in s3_con.buckets.all():
    print(bucket.name)
