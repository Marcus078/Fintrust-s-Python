import boto3
from datetime import datetime

s3 = boto3.client("s3")

BUCKET = "fintrust-cost-reports"


def write_monthly_report(
        report_text
):

    now = datetime.now()

    key = (
        f"{now.year}/"
        f"{now.month:02d}/"
        f"monthly_summary.txt"
    )

    s3.put_object(
        Bucket=BUCKET,
        Key=key,
        Body=report_text.encode(
            "utf-8"
        )
    )

    print(
        f"Written: s3://"
        f"{BUCKET}/{key}"
    )