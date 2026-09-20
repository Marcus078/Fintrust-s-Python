import json
import os
import logging
import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

sns = boto3.client('sns')

ALERT_TOPIC_ARN = os.environ['ALERT_TOPIC_ARN']

HIGH_RISK_THRESHOLD = float(
    os.environ.get(
        'HIGH_RISK_THRESHOLD',
        '75.0'
    )
)

def calculate_risk_score(txn):

    score = 0.0

    amount = float(txn.get('amount', 0))

    if amount > 50000:
        score += 40
    elif amount > 10000:
        score += 20
    elif amount > 1000:
        score += 5

    if txn.get('currency') != 'ZAR':
        score += 20

    desc = txn.get(
        'description',
        ''
    ).lower()

    for keyword in [
        'crypto',
        'wire',
        'urgent',
        'casino'
    ]:
        if keyword in desc:
            score += 15
            break

    return min(score, 100.0)

def lambda_handler(event, context):

    for record in event['Records']:

        txn = json.loads(
            record['body']
        )

        score = calculate_risk_score(txn)

        logger.info(
            f"Transaction {txn['id']} "
            f"risk score: {score}"
        )

        if score >= HIGH_RISK_THRESHOLD:

            sns.publish(
                TopicArn=ALERT_TOPIC_ARN,
                Subject=f"HIGH RISK: "
                        f"{txn['id']}",
                Message=json.dumps({
                    "transaction_id": txn["id"],
                    "account_id": txn.get(
                        "account_id"
                    ),
                    "amount": txn.get(
                        "amount"
                    ),
                    "currency": txn.get(
                        "currency"
                    ),
                    "risk_score": score
                })
            )

    return {
        "statusCode": 200
    }