import base64
import json

# Sample transaction data as a dictionary
transaction_data = {
    "id": 500,
    "type": "PAYMENT",
    "nameOrig": "C1666544278",
    "amount": 45200.50,
    "oldbalanceOrg": 50000,
    "newbalanceOrig": 4799.50,
    "nameDest": "M1230701703",
    "oldbalanceDest": 0,
    "newbalanceDest": 0,
    "isFraud": 1,
    "isFlaggedFraud":0
}

# Convert the dictionary to a JSON string
json_data = json.dumps(transaction_data)

# Encode the JSON string in base64
encoded_data = base64.b64encode(json_data.encode()).decode()

print(encoded_data)
