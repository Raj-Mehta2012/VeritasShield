import base64
import json
import boto3

# Initialize S3 client globally ~ available throughout the function
s3_client = boto3.client('s3')

def lambda_handler(event, context):
    # Loop over each record from the Kinesis stream
    for record in event['Records']:
        # Kinesis data is base64 encoded so decode here
        payload = base64.b64decode(record["kinesis"]["data"])
        # Convert the decoded payload to a dictionary
        transaction_data = json.loads(payload)

        # Process the transaction
        print("Received transaction:", transaction_data)
        
         # Example of a simple high-value transcations flag, makes it easier for companies to just run fraud-detection-model on flagged transactions 
        if transaction_data['amount'] > 30000:
            print("High value transaction detected:", transaction_data)
            # Store flagged transactions in S3
            store_in_s3(transaction_data, 'financial-transactions', f"flagged/{transaction_data['id']}.json")

    return 'Successfully processed records'

def store_in_s3(data, bucket, key):
    # Convert Python dictionary to JSON string
    json_data = json.dumps(data)
    # Store JSON data as a file in S3
    s3_client.put_object(Bucket=bucket, Key=key, Body=json_data)