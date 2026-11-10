"""
RECORD CHECK  -  my version
===========================

Name  : Diana Costea 
Lane  : Cyber      (delete two)
Date  : 16/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""
records = [
    {"label": "10.0.0.5", "value": 12, "limit": 400},
    {"label": "10.0.0.9", "value": 25, "limit": 500},
    {"label": "10.0.0.7", "value": 8, "limit": 200},
]  

def check_record(value, limit):

    """Calculate the difference, percentage and status."""

    difference = value - limit
    percent = (value / limit) * 100

    if value > limit:
        status = "OVER LIMIT"
    else:
        status = "OK"

    return difference, percent, status


def print_report(label, value, limit):

    """Print the label, values and calculated results."""

    difference, percent, status = check_record(value, limit)

    print(f"Source IP: {label}")
    print(f"Failed logins: {value}")
    print(f"Total attempts: {limit}")
    print(f"Difference: {difference}")
    print(f"Percent: {percent:.1f}%")
    print(f"Status: {status}")
    print()

'''
for record in records:                                                    
    print_report(record["label"], record["value"], record["limit"]) 
'''

def print_summary(over_limit):
    """Print the total number of records that were over the limit."""
    print(f"Records OVER LIMIT: {over_limit}")


over_limit = 0

with open("results.txt", "w") as f:
    for record in records:
        print_report(record["label"], record["value"], record["limit"])

        difference, percent, status = check_record(
            record["value"], record["limit"]
        )

        f.write(f"{record['label']},{status}\n")
        
print_summary(over_limit)

