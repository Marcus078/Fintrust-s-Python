import pandas as pd

df = pd.read_parquet(
    "s3://fintrust-processed/"
    "transactions/year=2024/"
    "month=06/"
    "transactions.parquet",
    engine="pyarrow"
)

high_value = df[
    df["is_high_value"] == True
]

print(
    f"High-value transactions: "
    f"{len(high_value)}"
)

print(
    high_value[
        [
            "account_id",
            "amount",
            "currency"
        ]
    ]
)

by_currency = (
    df.groupby("currency")["amount"]
      .sum()
      .reset_index()
)

by_currency.columns = [
    "currency",
    "total_amount"
]

print(by_currency)