# End-to-End ETL Pipeline (Python + PostgreSQL)

## 📌 Overview
This project implements a production-style ETL pipeline that ingests raw transaction data from CSV files, validates and transforms it using rule-based logic, and loads clean, quarantined, and rejected records into a PostgreSQL database.

## 🧱 Architecture
CSV → Extract → Transform → Load → PostgreSQL

## 🔧 Tech Stack
- Python
- pandas
- PostgreSQL
- SQLAlchemy

## 🔍 Transformation Logic
- **Valid records**: clean and trusted transactions
- **Quarantined records**: suspicious values (negative or extreme amounts)
- **Rejected records**: invalid schema (missing user_id, invalid timestamp)

## 🗄️ Database Tables
- `valid_transactions`
- `quarantined_transactions`
- `rejected_transactions`

## ▶️ How to Run
```bash
pip install -r requirements.txt
python main.py
