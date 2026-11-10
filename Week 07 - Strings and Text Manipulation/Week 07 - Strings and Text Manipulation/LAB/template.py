"""
RECORD CHECK  -  my version
===========================

Name  :  Diana Costea 
Lane  :  Cyber 
Date  :  05/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Write parse_line(raw_line) that cleans and parses one raw, messy line
#    into a dict. Handle inconsistent spacing and case - that is the whole
#    point of this week.
#
#    Also write status_of(...), shaped for your lane
#    (e.g. OVER LIMIT / WARNING / OK, or FLAGGED / OK). Give both a
#    one-line docstring.

def parse_line(raw_line):
    """Clean a login record and return a dictionary."""
    record = {}

    for piece in raw_line.strip().split(","):
        key, value = piece.split("=", 1)

        key = key.strip().lower()
        value = value.strip()

        if key == "attempts":
            value = int(value)
        else:
            value = value.lower()

        record[key] = value

    return record


def status_of(record):
    """Return FLAGGED for a failed login result, otherwise OK."""
    if record["result"] == "failed":
        return "FLAGGED"
    else:
        return "OK"


# ====================================================================== INPUT
with open("login_records.txt", "w") as f:
    f.write("  SRC=10.0.0.5,ATTEMPTS=12,RESULT=FAILED  \n")
    f.write("src = 10.0.0.9 , attempts = 2 , result = success\n")
    f.write(" Src=10.0.0.7, Attempts=5, Result=Failed\n")
    f.write("SRC =10.0.0.8,ATTEMPTS=1,RESULT=SUCCESS\n")
    f.write("  src=10.0.0.6 , ATTEMPTS = 8 , result=FaIlEd  \n")


# =============================================================== PROCESS + OUTPUT
# Parse and report on every record.

record_count = 0
flagged_count = 0

with open("login_records.txt") as f:
    for raw_record in f:
        record = parse_line(raw_record)
        status = status_of(record)

        record_count += 1

        if status == "FLAGGED":
            flagged_count += 1

        print(f"{record} — {status}")

print(f"{record_count} records, {flagged_count} flagged")

