import pandas as pd
import random
from faker import Faker

fake = Faker()

rows = []

for i in range(10000):

    amount = round(random.uniform(10, 10000), 2)
    user_id = random.randint(1, 5000)
    timestamp = fake.date_time_this_year()

    # Bad records
    if random.random() < 0.05:
        amount = -amount

    if random.random() < 0.03:
        user_id = None

    if random.random() < 0.02:
        timestamp = "invalid_date"

    rows.append({
        "transaction_id": i + 1,
        "user_id": user_id,
        "amount": amount,
        "currency": "INR",
        "timestamp": timestamp,
        "status": random.choice(
            ["SUCCESS", "PENDING", "FAILED"]
        )
    })

df = pd.DataFrame(rows)

df.to_csv(
    "data/raw/large_transactions.csv",
    index=False
)

print(f"Generated {len(df)} records")