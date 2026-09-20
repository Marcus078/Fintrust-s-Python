def lambda_handler(event, context):

    for record in event['Records']:

        bucket = record['s3']['bucket']['name']

        key = record['s3']['object']['key']

        size = record['s3']['object']['size']

        print(
            f"File uploaded: "
            f"s3://{bucket}/{key}"
        )

        print(f"Size: {size}")