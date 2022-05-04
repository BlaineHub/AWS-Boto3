import boto3

aws = boto3.session.Session(profile_name='developer',region_name='us-east-1')
ec2_con = aws.resource('ec2')

regions = ec2_con.meta.client.describe_regions()['Regions']
for region in regions:
    ec2_con=boto3.client('ec2',region['RegionName'])
    list_of_volids=[]
    f_prod_bkup={'Name':'tag:Prod','Values':['backup','Backup']}
    paginator = ec2_con.get_paginator('describe_volumes')
    for each_page in paginator.paginate(Filters=[f_prod_bkup]):
        for each_vol in each_page['Volumes']:
           list_of_volids.append(each_vol['VolumeId'])
    if len(list_of_volids) < 1:
        print('There are no Volume Ids in {}'.format(region['RegionName']))
        continue
    print('The list of Volume Ids in {} are '.format(region['RegionName']),list_of_volids)
    snapids=[]
    for each_volid in list_of_volids:
        print('Taking Snaps of {}'.format(each_volid))
        res=ec2_con.create_snapshot(
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
        
    waiter = ec2_con.get_waiter('snapshot_completed')
    waiter.wait(SnapshotIds=snapids)
    print('Successfully completed Snaps for Volumes  {}'.format(list_of_volids))