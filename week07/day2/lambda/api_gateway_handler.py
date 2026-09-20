import json

def lambda_handler(event, context):

    method = event['httpMethod']
    path = event['path']

    params = event.get('queryStringParameters') or {}

    body_str = event.get('body') or '{}'
    body = json.loads(body_str)

    return {
        'statusCode': 200,
        'body': json.dumps({
            'method': method,
            'path': path,
            'received': body
        })
    }
``