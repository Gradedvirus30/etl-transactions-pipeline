CREATE TABLE IF NOT EXISTS valid_transactions (
    transaction_id BIGINT PRIMARY KEY,
    user_id BIGINT NOT NULL,
    amount NUMERIC(12,2) NOT NULL,
    currency VARCHAR(3),
    timestamp TIMESTAMP,
    status VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS quarantined_transactions (
    transaction_id BIGINT,
    user_id BIGINT,
    amount NUMERIC(12,2),
    currency VARCHAR(3),
    timestamp TIMESTAMP,
    status VARCHAR(20),
    rejection_reason TEXT
);

CREATE TABLE IF NOT EXISTS rejected_transactions (
    transaction_id BIGINT,
    user_id BIGINT,
    amount NUMERIC(12,2),
    currency VARCHAR(3),
    timestamp TIMESTAMP,
    status VARCHAR(20),
    rejection_reason TEXT
);
