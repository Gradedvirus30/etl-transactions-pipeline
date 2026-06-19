from pathlib import Path

def generate_report(total, valid, quarantine, reject):

    success_rate = (valid / total) * 100

    report = f"""
ETL RUN REPORT

Total Records: {total}

Valid Records: {valid}
Quarantined Records: {quarantine}
Rejected Records: {reject}

Success Rate: {success_rate:.2f}%
"""

    Path("reports").mkdir(exist_ok=True)

    with open("reports/run_report.txt", "w") as f:
        f.write(report)