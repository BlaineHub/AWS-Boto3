import boto3
import csv
from pprint import pprint

aws=boto3.session.Session(profile_name='developer',region_name='us-east-1')
ec2_client=aws.client('ec2')

count=1
csv_ob=open('inventory.csv','w',newline='')
csv_w=csv.writer(csv_ob)
csv_w.writerow(['S_NO','INSTANCE_ID','INSTANCE_TYPE','LAUNCH_TIME','PRIVATE_IP','VOLUME_ID'])

for each in ec2_client.describe_instances()['Reservations']:
    for eac in each['Instances']:
            for ea in eac['BlockDeviceMappings']:
                csv_w.writerow([count, eac['InstanceId'],eac['InstanceType'],eac['LaunchTime'].strftime('%Y-%m-%d'),eac['PrivateIpAddress'], ea['Ebs']['VolumeId']])
                count+=1
csv_ob.close()
    
