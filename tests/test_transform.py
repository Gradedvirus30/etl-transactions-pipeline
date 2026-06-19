import pandas as pd
from etl.transform import transform_transactions


def test_valid_transaction():

    df = pd.DataFrame([
        {
            "transaction_id": 1,
            "user_id": 101,
            "amount": 500,
            "currency": "USD",
            "timestamp": "2025-01-01",
            "status": "SUCCESS"
        }
    ])

    valid_df, quarantine_df, reject_df = transform_transactions(df)

    assert len(valid_df) == 1
    assert len(quarantine_df) == 0
    assert len(reject_df) == 0

def test_negative_amount():

    df = pd.DataFrame([
        {
            "transaction_id": 2,
            "user_id": 102,
            "amount": -500,
            "currency": "INR",
            "timestamp": "2025-01-01",
            "status": "SUCCESS"
        }
    ])

    valid_df, quarantine_df, reject_df = transform_transactions(df)

    assert len(valid_df) == 0
    assert len(quarantine_df) == 1
    assert len(reject_df) == 0

def test_missing_user_id():

    df = pd.DataFrame([
        {
            "transaction_id": 3,
            "user_id": None,
            "amount": 500,
            "currency": "INR",
            "timestamp": "2025-01-01",
            "status": "SUCCESS"
        }
    ])

    valid_df, quarantine_df, reject_df = transform_transactions(df)

    assert len(valid_df) == 0
    assert len(quarantine_df) == 0
    assert len(reject_df) == 1