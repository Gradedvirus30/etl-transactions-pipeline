from sqlalchemy import create_engine


def load_to_postgres(df, table_name, db_url):
    """
    Loads a DataFrame into PostgreSQL.
    """

    engine = create_engine(db_url)

    df.to_sql(
        table_name,
        engine,
        if_exists="append",
        index=False
    )

    print(f"[LOAD] Inserted {len(df)} rows into {table_name}")
