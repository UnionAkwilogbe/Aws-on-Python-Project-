"""This script manages Amazon EC2 instances using the Boto3 Python SDK.
"""
# import statements
import boto3

# create ec2 resource and instance name
ec2 = boto3.resource('ec2')
instance_name = 'dct-ec2-hol1'

# store instance id
instance_id = None

# Check if instance which you are trying to create already exists
instances =ec2.instances.all()
instance_exists = False
# and only work with an instance that hasn't been terminated
for instance in instances:
    for tag in instance.tags:
        if tag['Key'] == 'Name' and tag['Value'] == instance_name:
            instance_exists = True
            instance_id = instance.id
            print(f"An instance named '{instance_name}' with id '{instance_id}' already exists")
            break
        if instance_exists:
            break
        



if not instance_exists:
# Launch a new EC2 instance if it hasn't already been created
    new_instance = ec2.create_instances(
            ImageId='ami-01f10c2d6bce70d90', # replace with a valid AMI ID
            MinCount=1,
            MaxCount=1,
            InstanceType ='t2.micro',
            KeyName='demokeypair', # replace with your key pair name 
            TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': instance_name
                    },
                ]
            },
         
        ]   
    )
    instance_id = new_instance[0].id
    print(f"Instance named '{instance_name}' with id '{instance_id}' created")
    
# Stop an instance
#ec2.Instance(instance_id).stop()
#print(f"Instance '{instance_name}-{instance_id}' stopped")

# Start an instance
#ec2.Instance(instance_id).start()
#print(f"Instance '{instance_name}-{instance_id}' started")

# Terminate an instance
ec2.Instance(instance_id).terminate()
print(f"Instance '{instance_name}-{instance_id}' terminated")