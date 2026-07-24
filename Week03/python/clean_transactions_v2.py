"""
Reads transaction data from CSV,
cleans and validates records,
writes cleaned CSV output,
creates a JSON summary,
and records activity in audit.log.
"""

import csv
import json
import logging
from pathlib import Path


# Logging Configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(name)s  %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.FileHandler("audit.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("fintrust.pipeline")

INPUT_FILE = Path("transactions.csv")
OUTPUT_FILE = Path("clean_transactions.csv")
SUMMARY_FILE = Path("transactions_summary.json")


def clean_row(row):
    """Validate and clean one transaction."""

    try:
        amount = float(row["amount"])

        if amount <= 0:
            raise ValueError("Amount must be greater than zero")

        return {
            "transaction_id": row["transaction_id"].strip(),
            "account_id": row["account_id"].strip(),
            "transaction_type": row["transaction_type"].strip().title(),
            "amount": round(amount, 2)
        }

    except ValueError as error:
        logger.warning(
            "Skipped transaction %s: %s",
            row.get("transaction_id", "UNKNOWN"),
            error
        )
        return None

    except KeyError as error:
        logger.error("Missing column: %s", error)
        return None


def process_transactions():

    cleaned_rows = []
    total_amount = 0

    try:

        logger.info("Starting transaction processing")

        with open(INPUT_FILE, "r", newline="", encoding="utf-8") as fin:
            reader = csv.DictReader(fin)

            for row in reader:
                cleaned = clean_row(row)

                if cleaned:
                    cleaned_rows.append(cleaned)
                    total_amount += cleaned["amount"]

    except FileNotFoundError:
        logger.error("Input file not found: %s", INPUT_FILE)
        print("ERROR: Input file not found.")
        return

    except PermissionError:
        logger.error("Permission denied when reading %s", INPUT_FILE)
        print("ERROR: File is currently locked.")
        return

    except Exception:
        logger.exception("Unexpected error while reading file")
        return

    else:

        with open(
            OUTPUT_FILE,
            "w",
            newline="",
            encoding="utf-8"
        ) as fout:

            fieldnames = [
                "transaction_id",
                "account_id",
                "transaction_type",
                "amount"
            ]

            writer = csv.DictWriter(
                fout,
                fieldnames=fieldnames
            )

            writer.writeheader()
            writer.writerows(cleaned_rows)

        summary = {
            "total_transactions": len(cleaned_rows),
            "total_amount": round(total_amount, 2)
        }

        with open(
            SUMMARY_FILE,
            "w",
            encoding="utf-8"
        ) as json_file:

            json.dump(
                summary,
                json_file,
                indent=4
            )

        logger.info(
            "Processing complete. %d records written.",
            len(cleaned_rows)
        )

    finally:
        logger.info("Transaction pipeline finished")


if __name__ == "__main__":
    process_transactions()
