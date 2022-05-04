import boto3

s3 = boto3.client('s3')
response = s3.delete_object(
    Bucket='blaine-test2',
    Key='file1'
)
print(response)


#Multiple File Deletes
response = s3.delete_objects(
    Bucket='blaine-test2',
    Delete = {
        'Objects':[
            {'Key':'file1'},
            {'Key':'file2'},
            {'Key':'file3'}
        ]
    }
)