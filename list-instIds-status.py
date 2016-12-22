#!/usr/bin/python
import boto3
### http://boto3.readthedocs.io/en/latest/guide/migrationec2.html#checking-what-instances-are-running
ec2 = boto3.resource('ec2')
regions = ['us-east-1','ap-southeast-1','ap-southeast-2','eu-central-1']
instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
for i in instances:
    print(i.id, i.instance_type)
