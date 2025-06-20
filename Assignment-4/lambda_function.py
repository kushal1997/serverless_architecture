import boto3
import datetime
from dateutil import parser

ec2 = boto3.client('ec2')
volume_id = "vol-0f67bb76551a34acc"
days_to_check = 30

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
    print(f" new snapshot created : {snapshot["SnapshotId"]}")

def deleteOldSnapshots():
    deleted_OldSnapshots = []
    snapshots = ec2.describe_snapshots(Filters=[
        {'Name': 'volume-id', 'Values': [volume_id]},
        {'Name' : 'tag:CreatedBy', 'Values': ['LambdaBackup']}
    ])['Snapshots']

    # print(snapshots)

    present_date_time = datetime.datetime.now(datetime.timezone.utc)

    # =================== for testing purpose -> START ==============
    # present_date_time = "2025-07-22 17:58:58.706041+00:00"
    # present_date_time = parser.parse(present_date_time)
    # ==================       END            =======================

    # print(present_date_time)
    for snap in snapshots:
        startTime = snap['StartTime']
        days_difference = (present_date_time-startTime).days
        
        if days_difference > days_to_check:
            print("older snaps :",snap['SnapshotId'],"difference in days : ",days_difference, "days")
            ec2.delete_snapshot(SnapshotId=snap['SnapshotId'])
            deleted_OldSnapshots.append(snap['SnapshotId'])
        
    if deleted_OldSnapshots:
        print("All deleted snapshots are : ",deleted_OldSnapshots)
    else:
        print("There are no older snapshots to delete")

def lambda_handler(event, context):
    create_snapshot()
    deleteOldSnapshots()

# ============ for localy running code - comment the above lambda_handler & uncomment below ones ==============
# create_snapshot()
# deleteOldSnapshots()