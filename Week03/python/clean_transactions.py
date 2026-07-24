"""
Reads a transactions CSV file, cleans and validates records,
writes a cleaned CSV file, and generates a JSON summary.
"""

import csv
import json
from pathlib import Path


INPUT_FILE = Path("transactions.csv")
OUTPUT_FILE = Path("clean_transactions.csv")
SUMMARY_FILE = Path("transactions_summary.json")


def clean_row(row):
    """Validate and clean a transaction row."""

    try:
        amount = float(row["amount"])

        if amount <= 0:
            return None

        return {
            "transaction_id": row["transaction_id"].strip(),
            "account_id": row["account_id"].strip(),
            "transaction_type": row["transaction_type"].strip().title(),
            "amount": round(amount, 2)
        }

    except (ValueError, KeyError):
        return None


def process_transactions():
    """Read CSV, clean data, write output, create summary."""

    cleaned_rows = []
    total_amount = 0

    with open(INPUT_FILE, "r", newline="", encoding="utf-8") as fin:
        reader = csv.DictReader(fin)

        for row in reader:
            cleaned = clean_row(row)

            if cleaned:
                cleaned_rows.append(cleaned)
                total_amount += cleaned["amount"]

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as fout:
        fieldnames = [
            "transaction_id",
            "account_id",
            "transaction_type",
            "amount"
        ]

        writer = csv.DictWriter(fout, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(cleaned_rows)

    summary = {
        "total_transactions": len(cleaned_rows),
        "total_amount": round(total_amount, 2)
    }

    with open(SUMMARY_FILE, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=4)

    print("Transaction cleaning complete.")
    print(f"Valid transactions: {len(cleaned_rows)}")
    print(f"Total amount: R{total_amount:,.2f}")
    print(f"Clean CSV: {OUTPUT_FILE}")
    print(f"JSON Summary: {SUMMARY_FILE}")


if __name__ == "__main__":
    process_transactions()
