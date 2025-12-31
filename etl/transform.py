import pandas as pd


def transform_transactions(df: pd.DataFrame):
    """
    Cleans and validates transaction data.
    Returns: valid_df, quarantine_df, reject_df
    """

    df = df.copy()

    # Track rejection reasons
    df["rejection_reason"] = ""

    # -------------------------------
    # BASIC SCHEMA VALIDATION
    # -------------------------------
    required_columns = {
        "transaction_id",
        "user_id",
        "amount",
        "currency",
        "timestamp",
        "status"
    }

    if not required_columns.issubset(df.columns):
        missing = required_columns - set(df.columns)
        raise ValueError(f"[TRANSFORM ERROR] Missing columns: {missing}")

    # -------------------------------
    # TYPE CONVERSIONS
    # -------------------------------
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")

    # -------------------------------
    # REJECTION RULES (HARD FAIL)
    # -------------------------------
    reject_mask = (
        df["transaction_id"].isna() |
        df["user_id"].isna() |
        df["timestamp"].isna()
    )

    df.loc[df["transaction_id"].isna(), "rejection_reason"] += "missing_transaction_id;"
    df.loc[df["user_id"].isna(), "rejection_reason"] += "missing_user_id;"
    df.loc[df["timestamp"].isna(), "rejection_reason"] += "invalid_timestamp;"

    reject_df = df[reject_mask]

    # -------------------------------
    # QUARANTINE RULES (SUSPICIOUS)
    # -------------------------------
    quarantine_mask = (
        (df["amount"] <= 0) |
        (df["amount"] > 1_000_000)
    )

    quarantine_df = df[~reject_mask & quarantine_mask]

    # -------------------------------
    # VALID RECORDS
    # -------------------------------
    valid_df = df[~reject_mask & ~quarantine_mask]

    print(f"[TRANSFORM] Valid: {len(valid_df)} | Quarantine: {len(quarantine_df)} | Reject: {len(reject_df)}")

    return valid_df, quarantine_df, reject_df
