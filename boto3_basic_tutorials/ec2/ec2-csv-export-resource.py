import boto3
import csv

aws=boto3.session.Session(profile_name='developer',region_name='us-east-1')
ec2_resource=aws.resource('ec2')

count=1
csv_ob=open('inventory.csv','w',newline='')
csv_w=csv.writer(csv_ob)
csv_w.writerow(['S_NO','INSTANCE_ID','INSTANCE_TYPE','LAUNCH_TIME','PRIVATE_IP'])

for each in ec2_resource.instances.all():
    print(count,each.instance_id,each.instance_type,each.launch_time.strftime('%Y-%m-%d'),each.private_ip_address)
    csv_w.writerow([count,each.instance_id,each.instance_type,each.launch_time.strftime('%Y-%m-%d'),each.private_ip_address])
    count+=1
csv_ob.close()

