import sys
import time
from etl.extract import extract_csv
from etl.transform import transform_transactions
from etl.load import load_to_postgres
from etl.logger import logger
from etl.metrics import generate_report


from etl.config import DB_URL


if __name__ == "__main__":
    start_time = time.time()
    logger.info("Pipeline started")
    
    file_name = sys.argv[1] if len(sys.argv) > 1 else "transactions.csv"
    file_path = f"data/raw/{file_name}"

    logger.info(f"Input file: {file_name}")

    df = extract_csv(file_path)
    logger.info(f"Extracted {len(df)} records")


    valid_df, quarantine_df, reject_df = transform_transactions(df)
    logger.info(
    f"Valid={len(valid_df)} "
    f"Quarantine={len(quarantine_df)} "
    f"Reject={len(reject_df)}"
    )
    generate_report(
    len(df),
    len(valid_df),
    len(quarantine_df),
    len(reject_df)
    )
    


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
    logger.info("Pipeline completed successfully")
    end_time = time.time()

    runtime = end_time - start_time

    print(f"Pipeline runtime: {runtime:.2f} seconds")

    logger.info(
        f"Pipeline runtime: {runtime:.2f} seconds"
    )