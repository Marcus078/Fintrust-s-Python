import boto3
import json
from datetime import datetime

s3 = boto3.client("s3")

BUCKET = "fintrust-governance"


def write_report(summary):

    today = datetime.now()

    key = (
        f"tag-audit/"
        f"{today:%Y-%m-%d}.json"
    )

    s3.put_object(
        Bucket=BUCKET,
        Key=key,
        Body=json.dumps(
            summary,
            indent=2
        )
    )

    print(
        f"Uploaded "
        f"s3://{BUCKET}/{key}"
    )