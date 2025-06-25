import boto3
import datetime

import os
# from dotenv import load_dotenv
# load_dotenv()

def delete_old_files():
    bucket_name = os.environ["BUCKET_NAME"]
    days_to_check = 30

    s3 = boto3.client('s3')
    response = s3.list_objects_v2(Bucket=bucket_name)

    deleted_old_files = []
    present_date_time = datetime.datetime.now(datetime.timezone.utc)

    # print("response ===", response, "current date & time ====", present_date_time)

    for content in response['Contents']:
        last_modified = content['LastModified']
        days_difference = (present_date_time - last_modified).days

        print(f'difference in days for {content['Key']} is {days_difference}')

        if days_difference > days_to_check:
            print(f"deleting old files {content["Key"]} having days difference of {days_difference} days")
            s3.delete_object(Bucket=bucket_name, Key=content['Key'])
            deleted_old_files.append(content['Key'])
        
    

    if deleted_old_files:
        print("all deleted old files are: ",deleted_old_files)
    else:
        print("There are no older files to delete")

def lambda_handler(event, context):
    delete_old_files()


