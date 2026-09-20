import boto3
import json

sqs = boto3.client(
    'sqs',
    region_name='af-south-1'
)

comp = boto3.client(
    'comprehend',
    region_name='af-south-1'
)

URGENT_QUEUE_URL = (
    'https://sqs.af-south-1.amazonaws.com/'
    'ACCOUNT_ID/'
    'fintrust-support-urgent'
)

STANDARD_QUEUE_URL = (
    'https://sqs.af-south-1.amazonaws.com/'
    'ACCOUNT_ID/'
    'fintrust-support-standard'
)


def redact_pii(text):

    response = comp.detect_pii_entities(
        Text=text,
        LanguageCode='en'
    )

    entities = response['Entities']

    entities.sort(
        key=lambda x:
        x['BeginOffset'],
        reverse=True
    )

    detected_types = []

    text_chars = list(text)

    for entity in entities:

        detected_types.append(
            entity['Type']
        )

        replacement = (
            f'[{entity["Type"]}]'
        )

        text_chars[
            entity['BeginOffset']:
            entity['EndOffset']
        ] = list(replacement)

    return (
        ''.join(text_chars),
        detected_types
    )


def process_support_ticket(
        ticket_text
):

    redacted_text, pii_types = (
        redact_pii(ticket_text)
    )

    sentiment_resp = (
        comp.detect_sentiment(
            Text=ticket_text,
            LanguageCode='en'
        )
    )

    sentiment = (
        sentiment_resp['Sentiment']
    )

    queue_url = (
        URGENT_QUEUE_URL
        if sentiment == 'NEGATIVE'
        else STANDARD_QUEUE_URL
    )

    message = {
        'redacted_text':
            redacted_text,
        'sentiment':
            sentiment,
        'pii_types_found':
            pii_types,
        'priority':
            (
                'HIGH'
                if sentiment == 'NEGATIVE'
                else 'STANDARD'
            )
    }

    sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=json.dumps(
            message
        )
    )

    return message