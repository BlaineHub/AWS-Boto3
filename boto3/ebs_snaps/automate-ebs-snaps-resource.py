import boto3

aws = boto3.session.Session(profile_name='developer',region_name='us-east-1')
ec2_con=aws.resource('ec2','us-east-1')

vol_ids=[]
f_prod_bkup={'Name':'tag:Prod','Values':['backup','Backup']}
for each_vol in ec2_con.volumes.filter(Filters=[f_prod_bkup]):
        vol_ids.append(each_vol.id)
print('The list of Volume Ids are ',vol_ids)

snap_ids=[]
for each_vol_id in vol_ids:
    print('Taking Snaps of {}'.format(each_vol_id))
    res=ec2_con.create_snapshot(
            Description='Taking snap with Lambda and CW',
            VolumeId = each_vol_id,
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
    snap_ids.append(res.id)
print('The Snap Ids are: ',snap_ids)

ec2_client=aws.client('ec2','us-east-1')
    
waiter = ec2_client.get_waiter('snapshot_completed')
waiter.wait(SnapshotIds=snap_ids)
print('Successfully completed Snaps for Volumes  {}'.format(vol_ids))
