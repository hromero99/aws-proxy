import logging
import boto3
from botocore.exceptions import ClientError

def upload_file():
    s3 = boto3.client('s3')
    with open("FILE_NAME", "rb") as f:
        s3.upload_fileobj(f, "BUCKET_NAME", "OBJECT_NAME")