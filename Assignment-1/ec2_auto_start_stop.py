import boto3

ec2 = boto3.client('ec2')

def auto_stop_ec2():
    stop_response = ec2.describe_instances(
    Filters=[
            {'Name': 'tag:Action', 'Values': ['Auto-Stop']},
            {'Name': 'instance-state-name', 'Values': ['running']}
        ]
    )
    # print(stop_response)

    stop_ids = [instance['InstanceId']
        for reservation in stop_response['Reservations']
        for instance in reservation['Instances']]

    print(stop_ids)

    if stop_ids:
        ec2.stop_instances(InstanceIds=stop_ids)
        print("Auto-stopped ec2 instances are : ",stop_ids)
    else:
        print("No ec2 running with Auto Stop action found")

def auto_start_stop_ec2():
    auto_stop_ec2()

auto_start_stop_ec2()