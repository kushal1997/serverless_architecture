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

def auto_start_ec2():
    start_respose = ec2.describe_instances(
        Filters=[
            {'Name': 'tag:Action', 'Values': ['Auto-Start']},
            {'Name': 'instance-state-name', 'Values': ['stopped']}
        ]
    )

    start_ids = [instance['InstanceId']
                 for reservation in start_respose['Reservations']
                 for instance in reservation['Instances']]
    print(start_ids)

    if start_ids:
        ec2.start_instances(InstanceIds=start_ids)
        print("Auto-started ec2 instances are : ",start_ids)
    else:
        print("No ec2 with Auto-Start action stopped")


def auto_manage_ec2():
    # auto_stop_ec2()
    auto_start_ec2()

auto_manage_ec2()