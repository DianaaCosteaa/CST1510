"""
RECORD CHECK  -  my version
===========================

Name  : Diana Costea
Lane  : Cyber 
Date  : 23/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ====================================================================== CLASS
# 1. Define a class called Record.

# add over_limit_count as a class-level running total
from pathlib import Path

class Record:
    """Represent a record and count objects that reach their limits."""

    over_limit_count = 0

    def __init__(self, label, value, limit):
        """Store the attributes and count records over the limit."""
        self.label = label
        self.value = value
        self.limit = limit

        if self.status() == "OVER LIMIT":
            Record.over_limit_count += 1

    def status(self):
        """Return the status based on the percentage of the limit."""
        percent = (self.value / self.limit) * 100

        if percent >= 100:
            return "OVER LIMIT"
        elif percent >= 90:
            return "WARNING"
        else:
            return "OK"


# ==================================================================== RECORDS
# 2. Create your records.
#
#     instead, write load_records(path) that reads label,value,limit
#     lines from a file and returns a list of Record objects. Make
#     your own data file, one record per line.

def load_records(path):
    """Read a file and return a list of Record objects."""
    records = []

    with open(path) as f:
        for line in f:
            label, value, limit = line.strip().split(",")

            value = float(value)
            limit = float(limit)

            record = Record(label, value, limit)
            records.append(record)

    return records


records = load_records(Path(__file__).parent / "records_sample.txt")


# ==================================================================== OUTPUT
# 3. Print a report for each record.

#        also keep a running count of how many came back OVER LIMIT
#        across every record, and print that once, after the loop.
#        (Simplest: a plain variable outside the loop, same pattern
#        as Week 4. If you want it to live ON the object instead,
#        that is a stretch worth trying - but a variable is enough.)

for record in records:
    status = record.status()

    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)

    print(f"Source IP: {record.label}")
    print(f"Failed logins: {record.value}")
    print(f"Total attempts: {record.limit}")
    print(f"Percent: {(record.value / record.limit) * 100:.1f}%")
    print(f"Status: {status}")

    print("=" * 34)

print(f"{Record.over_limit_count} of {len(records)} records are OVER LIMIT")


