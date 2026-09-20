import time
import boto3

from functools import wraps

s3 = boto3.client("s3")


def retry(max_attempts=3, delay_seconds=1):

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            last_error = None

            for attempt in range(max_attempts):

                try:
                    return func(*args, **kwargs)

                except Exception as e:

                    last_error = e

                    wait = delay_seconds * (2 ** attempt)

                    print(
                        f"Attempt {attempt + 1} failed: {e}"
                    )

                    time.sleep(wait)

            raise last_error

        return wrapper

    return decorator


@retry(max_attempts=3, delay_seconds=1)
def get_bucket_info(bucket_name):

    return s3.head_bucket(
        Bucket=bucket_name
    )


if __name__ == "__main__":

    response = get_bucket_info(
        "fintrust-raw-data"
    )

    print(response)