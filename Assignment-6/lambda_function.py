import boto3
from datetime import datetime,timedelta

def lambda_handler(event,context):
    cloudWatch = boto3.client('cloudwatch', region_name='us-east-1')
    sns = boto3.client('sns')

    max_amount = 1
    sns_topic_arn = "SNS_TOPIC_ARN"

    res = cloudWatch.get_metric_statistics(
        Namespace='AWS/Billing',
        MetricName='EstimatedCharges',
        Dimensions=[{'Name': 'Currency', 'Value': 'USD'}],
        StartTime=datetime.now() - timedelta(days=1),
        EndTime=datetime.now(),
        Period=86400,
        Statistics=['Maximum']
    )
    datapoints = res['Datapoints']

    if datapoints:
        latest_billing_amount = datapoints[0]['Maximum']

        if latest_billing_amount > max_amount:
            message = f"AWS billing alert \n\n Current charges: {latest_billing_amount}$\n Threshold: {max_amount}$"
            # print(message)
            sns.publish(TopicArn=sns_topic_arn, Message=message, Subject="!!! Aws Billing Alert")
            print("Alert Sent !!! ")
        else:
            print("Billing is all under control")
    else:
        print("no billling data found")



# ------------- only for running code locally ---------------------
# if __name__ == "__main__":
#     lambda_handler(None, None)
# ------------------------------------------------------------------

