from etl.extract import extract_csv
from etl.transform import transform_transactions
from etl.load import load_to_postgres


DB_URL = "postgresql://postgres:M%40may2006@localhost:5432/etl_db"

if __name__ == "__main__":
    df = extract_csv("data/raw/transactions.csv")

    valid_df, quarantine_df, reject_df = transform_transactions(df)

    load_to_postgres(
        valid_df.drop(columns=["rejection_reason"]),
        "valid_transactions",
        DB_URL
    )

    load_to_postgres(
        quarantine_df,
        "quarantined_transactions",
        DB_URL
    )

    load_to_postgres(
        reject_df,
        "rejected_transactions",
        DB_URL
    )

