import boto3
import sys

source_region='us-east-1'
dest_region='us-east-2'


aws = boto3.session.Session(profile_name='developer',region_name='us-east-1')
ec2_con_source=aws.client('ec2',source_region)
sts_client = aws.client(service_name='sts')
acc_id = sts_client.get_caller_identity()['Account']

f_bkup={'Name':'tag:Backup','Values':['Yes']}
bkup_snaps=[]
for each_snap in ec2_con_source.describe_snapshots(Filters=[f_bkup],OwnerIds=[acc_id])['Snapshots']:
    bkup_snaps.append(each_snap['SnapshotId'])

if len(bkup_snaps)<1:
    print('There are no snaps to be backed up')
    sys.exit(0)

ec2_con_dest=aws.client('ec2',dest_region)

new_snap_ids=[]
for each_snap in bkup_snaps:
    print('Taking backup of {} into {}'.format(each_snap,dest_region))
    res = ec2_con_dest.copy_snapshot(
        Description='Disaster Recovery',
        SourceRegion=source_region,
        SourceSnapshotId = each_snap
    )
    new_snap_ids.append(res['SnapshotId'])


waiter = ec2_con_dest.get_waiter('snapshot_completed')
waiter.wait(SnapshotIds=new_snap_ids)
print('Successfully completed migration for {}'.format(bkup_snaps))
print('Modifying tags to backup completed')

for each_snap in bkup_snaps:
    ec2_con_source.delete_tags(
            Resources = [each_snap],
            Tags=[
                {
                    'Key':'Backup',
                    'Value':'Yes'
                },
            ]
        )
    ec2_con_source.create_tags(
                    Resources = [each_snap],
                Tags=[
                    {
                        'Key':'Backup',
                        'Value':'Completed'
                    },
                ]
            )
print('Tag change completed for snaps {}'.format(bkup_snaps))



