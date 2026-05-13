import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'priyanka2211')
    AWS_REGION = 'ap-south-1'
    DYNAMODB_TABLE = 'todo_tasks'
    SNS_TOPIC_ARN = os.getenv("SNS_TOPIC_ARN")
    EMAIL = "priyankachauhan.959124@gmail.com"
