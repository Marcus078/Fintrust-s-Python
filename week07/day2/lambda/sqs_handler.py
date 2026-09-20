import json

def lambda_handler(event, context):

    for record in event['Records']:

        body = json.loads(record['body'])

        print(
            f"Processing message "
            f"{record['messageId']}"
        )

        print(body)