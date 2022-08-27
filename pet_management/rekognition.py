import os

import boto3
import environ
import requests

from pet_management.models import PetCategory

env = environ.Env()
environ.Env.read_env()

AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
AWS_SECRET_KEY = os.getenv('AWS_SECRET_KEY')
AWS_REGION_NAME = os.getenv('AWS_REGION_NAME')
BUCKET_S3 = os.getenv('BUCKET_S3')


def upload_picture_to_bucket(url, photo):
    s3 = boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY,
        region_name=AWS_REGION_NAME,
    )
    r = requests.get(url, stream=True)
    s3.upload_fileobj(r.raw, BUCKET_S3, photo)


def category_detection(photo):
    client = boto3.client(
        'rekognition',
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY,
        region_name=AWS_REGION_NAME,
    )

    response = client.detect_labels(
        Image={
            'S3Object': {
                'Bucket': BUCKET_S3,
                'Name': photo,
            },
        },
        MaxLabels=10,
    )
    category_detections = []
    for label in response['Labels']:
        if label['Confidence'] > 50:
            category_detections.append(label['Name'])
    availabe_categories = ['Dog', 'Cat', 'Parrot']
    for available_category in availabe_categories:
        if available_category in category_detections:
            pet_category = PetCategory.objects.get(name=available_category)
            return pet_category.id
    return 1
