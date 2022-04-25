import json
import boto3

def lambda_handler(event, context):
    ec2_client=boto3.client('ec2','us-east-1')
    list_of_volids=[]
    f_prod_bkup={'Name':'tag:Prod','Values':['backup','Backup']}
    paginator = ec2_client.get_paginator('describe_volumes')
    for each_page in paginator.paginate(Filters=[f_prod_bkup]):
        for each_vol in each_page['Volumes']:
           list_of_volids.append(each_vol['VolumeId'])
    print('The list of Volume Ids are ',list_of_volids)
    
    snapids=[]
    for each_volid in list_of_volids:
        print('Taking Snaps of {}'.format(each_volid))
        res=ec2_client.create_snapshot(
                Description='Taking snap with Lambda and CW',
                VolumeId = each_volid,
                TagSpecifications=[
                    {
                        'ResourceType':'snapshot',
                        'Tags':[
                            {
                                'Key':'Delete-on',
                                'Value':'90'
                            }
                               ]
                    }
                   ]
                  )
        snapids.append(res['SnapshotId'])
    print('The Snap Ids are: ',snapids)
        
    waiter = ec2_client.get_waiter('snapshot_completed')
    waiter.wait(SnapshotIds=snapids)
    print('Successfully completed Snaps for Volumes  {}'.format(list_of_volids))