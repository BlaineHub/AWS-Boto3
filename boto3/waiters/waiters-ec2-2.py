import boto3

aws_console = boto3.session.Session(profile_name='developer',region_name='us-east-1')
ec2_console = aws_console.resource('ec2')

'''
for each in ec2_console.instances.all():
    print(each.id)

for each in ec2_console.instances.limit(1):
    print(each.id)
'''

f1= {'Name': "instance-state-name", "Values":['running']}
f2= {'Name':'instance-type','Values':['t2.micro']}
for each in ec2_console.instances.filter(Filters=[f1,f2]):
    print(each.id)

