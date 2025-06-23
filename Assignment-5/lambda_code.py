import boto3
from datetime import datetime

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name='us-west-2')

    instances = event['detail']['instance-id']

    present_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(present_date)
    tags = [
        {'Key': 'LaunchDate', 'Value': present_date},
        {'Key': 'Assignment5', 'Value': 'AutoTagged'}
    ]

    ec2.create_tags(Resources=[instances], Tags=tags)

    print(f"Tagged EC2 Instance {instances} with {tags}")
    return {
        'statusCode': 200,
        'body': f"Successfully tagged instance {instances}"
    }

# ------------- only for running code locally ---------------------
if __name__ == "__main__":
    fake_event = {
        'detail': {
            'instance-id': 'i-04e5afa4082ea2473'
        }
    }
    lambda_handler(fake_event, None)
# ------------------------------------------------------------------
