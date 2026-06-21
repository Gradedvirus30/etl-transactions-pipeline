# ETL Transactions Pipeline

OVERVIEW

This project implements a modular ETL (Extract, Transform, Load) pipeline for processing transaction data from CSV files and loading validated records into PostgreSQL.

The pipeline performs data validation, categorizes records based on quality rules, generates execution reports, logs pipeline activity, and supports testing with both real and synthetic datasets.

The goal of the project was to explore practical data engineering concepts such as data validation, data quality monitoring, database loading, logging, testing, and performance benchmarking.

---

ARCHITECTURE

CSV Input
|
v
Extract
|
v
Transform & Validation
|
+-- Valid Records
+-- Quarantined Records
+-- Rejected Records
|
v
Data Quality Report
|
v
PostgreSQL

---

FEATURES

* Modular ETL architecture
* CSV-based transaction ingestion
* Schema validation and data quality checks
* Separation of valid, quarantined, and rejected records
* PostgreSQL integration using SQLAlchemy
* Environment variable based configuration
* Execution logging
* Automated run reports
* Unit testing using pytest
* Synthetic dataset generation for benchmarking
* Configurable input datasets

---

TECH STACK

* Python
* Pandas
* PostgreSQL
* SQLAlchemy
* Pytest
* Faker
* python-dotenv

---

VALIDATION RULES

Rejected Records

* Missing transaction_id
* Missing user_id
* Invalid timestamp

Quarantined Records

* Amount <= 0
* Amount exceeds predefined limits

Valid Records

* Records that pass all validation checks

---

DATABASE TABLES

valid_transactions

* Stores trusted records that pass validation.

quarantined_transactions

* Stores suspicious records requiring review.

rejected_transactions

* Stores records that fail schema validation.

---

PROJECT STRUCTURE

etl_transactions/

|-- data/
|   |-- raw/
|   |-- processed/
|
|-- etl/
|   |-- extract.py
|   |-- transform.py
|   |-- load.py
|   |-- logger.py
|   |-- metrics.py
|   |-- config.py
|   |-- **init**.py
|
|-- tests/
|   |-- test_transform.py
|
|-- generate_data.py
|-- main.py
|-- requirements.txt
|-- README.md

---

CONFIGURATION

Create a .env file in the project root:

DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=etl_db

---

RUNNING THE PIPELINE

Default dataset:

python main.py

Custom dataset:

python main.py large_transactions.csv

---

LOGGING

Pipeline execution details are written to:

etl.log

Example:

INFO | Pipeline started
INFO | Input file: large_transactions.csv
INFO | Extracted 10000 records
INFO | Valid=8971 Quarantine=486 Reject=543
INFO | Pipeline completed successfully

---

DATA QUALITY REPORTING

Each run generates a report containing:

* Total records processed
* Valid records
* Quarantined records
* Rejected records
* Success rate

Example:

Total Records: 10000

Valid Records: 8971
Quarantined Records: 486
Rejected Records: 543

Success Rate: 89.71%

---

UNIT TESTING

Tests currently cover:

* Valid transaction handling
* Quarantine rule validation
* Rejection rule validation

Run tests using:

python -m pytest

---

SYNTHETIC DATA GENERATION

Synthetic transaction datasets can be generated using:

python generate_data.py

Generated datasets intentionally contain corrupted records to validate quarantine and rejection logic at larger scales.

---

PERFORMANCE BENCHMARK

## Dataset Size          Runtime

1,000 Records         0.55 s
10,000 Records        0.73 s

Benchmarks were executed on a local development machine using PostgreSQL and Pandas.

---

POTENTIAL EXTENSIONS

* Docker containerization
* Batch database loading
* Incremental data processing
* Cloud database deployment
* Workflow orchestration using Apache Airflow
* Dashboard for monitoring ETL runs

---

LEARNING OUTCOMES

Through this project I gained practical experience with:

* ETL pipeline design
* Data validation and cleansing
* PostgreSQL integration
* Configuration management
* Logging and monitoring
* Unit testing
* Synthetic data generation
* Performance benchmarking
* Python project structuring
