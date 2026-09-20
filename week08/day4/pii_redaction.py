import boto3

comp = boto3.client(
    'comprehend',
    region_name='af-south-1'
)

def redact_pii(text):

    response = comp.detect_pii_entities(
        Text=text,
        LanguageCode='en'
    )

    entities = response['Entities']

    entities.sort(
        key=lambda e:
        e['BeginOffset'],
        reverse=True
    )

    detected_types = list(
        {
            e['Type']
            for e in entities
        }
    )

    text_chars = list(text)

    for entity in entities:

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


ticket = (
    "My name is Sipho Nkosi and "
    "my account number is "
    "ACC-7823041. "
    "My ID number is "
    "9203045678082."
)

redacted, pii_types = redact_pii(ticket)

print(redacted)
print(pii_types)