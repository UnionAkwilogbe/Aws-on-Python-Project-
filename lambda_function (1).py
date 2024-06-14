import json
import boto3
import logging
from datetime import datetime

logger = logging.getlogger()
logger.setlevel(logging.INFO)

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    current_data = datetime.now().strftime("%Y-%m-%d")
    
    try:
        response = ec2.create_snapshot(
            VolumeId='vol-065099a44e3d25537',
            Description='My Ec2 Snapshot',
            TagSpecifications=[
                {
                    'ResourceType':  'snapshot',
                    'Tags': [ 
                        {
                            'Key' : 'Name',
                            'Value': f"My Ec2 snapshot {current_date}"
                            }
                        
                        ]
                    
                    }
                
                ]
            
            )
        logger.info(f"Successfully created snapshot: {json.dumps(response, defaulte=str)}")
    
    except Exception as e:
        logger.error(f"Error creating snapshot: {str(e)}")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
