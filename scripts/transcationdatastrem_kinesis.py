import boto3
import json
import random
from datetime import datetime
from dotenv import load_dotenv
import os
import pandas as pd
import openpyxl

# Load environment variables from .env file
load_dotenv()

# Retrieve environment variables
aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
aws_default_region = os.getenv('AWS_DEFAULT_REGION')

# Initialize a Kinesis client with AWS SDK
kinesis_client = boto3.client('kinesis', region_name=aws_default_region)

# Load your dataset
data = pd.read_excel('data/Fraud_Transactions.xlsx')

# Function to send data to Kinesis
def send_to_kinesis(row):
    data = json.dumps(row.to_dict())
    kinesis_client.put_record(
        StreamName='TransactionStream',
        Data=data,
        PartitionKey=str(row['id']) #Unique identifier
    )

# Stream data to Kinesis
data.apply(send_to_kinesis, axis=1)