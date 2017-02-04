#!/usr/bin/python
#import boto3
import boto.ec2

# If you need to connect to one region, you can uncomment the below line and then comment the first 'for'
# loop and then the line 'regions'. Also, you will need to comment conn=boto.ec2.connect_to_region(u)

#conn=boto.ec2.connect_to_region("eu-central-1") 

regions = ['us-east-1','ap-southeast-1','ap-southeast-2','eu-central-1']
# First loop, connects to all regions
for u in regions:
        conn=boto.ec2.connect_to_region(u)
# with the conn variable, we are getting all instances available from first for loop
        reservations = conn.get_all_instances()
        for res in reservations:
                for inst in res.instances:
                        if 'Name' in inst.tags:
                                print "%s (%s) [%s]" % (inst.tags['Name'], inst.id, inst.state)
                        else:
                                print "%s [%s]" % (inst.id, inst.state)
