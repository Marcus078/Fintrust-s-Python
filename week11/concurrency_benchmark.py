import time
import boto3

from concurrent.futures import (
    ThreadPoolExecutor,
    as_completed
)

s3 = boto3.client("s3")

BUCKET = "fintrust-raw-data"

KEYS = [
    "file1.csv",
    "file2.csv",
    "file3.csv",
    "file4.csv",
    "file5.csv"
]


def get_metadata(key):

    response = s3.head_object(
        Bucket=BUCKET,
        Key=key
    )

    return {
        "key": key,
        "size": response["ContentLength"]
    }


def sequential():

    start = time.perf_counter()

    results = [
        get_metadata(key)
        for key in KEYS
    ]

    end = time.perf_counter()

    print(
        f"Sequential: "
        f"{end - start:.2f}s"
    )

    return results


def threaded():

    start = time.perf_counter()

    results = []

    with ThreadPoolExecutor(
        max_workers=5
    ) as executor:

        futures = {
            executor.submit(
                get_metadata,
                key
            ): key
            for key in KEYS
        }

        for future in as_completed(
            futures
        ):

            results.append(
                future.result()
            )

    end = time.perf_counter()

    print(
        f"Threaded: "
        f"{end - start:.2f}s"
    )

    return results


if __name__ == "__main__":

    sequential()
    threaded()