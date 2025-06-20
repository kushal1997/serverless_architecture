import boto3
import datetime

ec2 = boto3.client('ec2')
volume_id = "vol-0f67bb76551a34acc"
total_days = 30

def create_snapshot():
    snapshot = ec2.create_snapshot(
        VolumeId=volume_id,
        Description=f"backup for {volume_id}",
        TagSpecifications=[
            {
                'ResourceType': 'snapshot',
                'Tags': [
                    {'Key': 'CreatedBy', 'Value': 'LambdaBackup'}
                ]
            }
        ]
    )
    print(f"snapshot: {snapshot["SnapshotId"]}")

create_snapshot()