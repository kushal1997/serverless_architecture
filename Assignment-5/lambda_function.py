import boto3
from datetime import datetime

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')

    try:
        instances = event['detail']['instance-id']
    except KeyError:
        return {"status": "no instance found"}
    
    present_date = datetime.now().strftime('%Y-%m-%d')
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
# if __name__ == "__main__":
#     fake_event = {
#         'detail': {
#             'instance-id': 'i-0d68e10ecdcb9513a'
#         }
#     }
#     lambda_handler(fake_event, None)
# ------------------------------------------------------------------
