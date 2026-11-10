"""
RECORD CHECK  -  my version
===========================

Name  :  Diana Costea
Lane  :  AI / Cyber / IT      (delete two)
Date  :  09/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Write a function called status_of(percent) that returns "OVER LIMIT"
#    (100% or more), "WARNING" (90% or more), or "OK" (anything else).
#
#    Typical and above: also write check(value, limit) that returns the
#    difference and the percentage as two values - do not print anything
#    inside it, only calculate and return.
#
#    Excellent: also write print_report(label, value, limit, difference,
#    percent, status) that does ALL of the printing below - nothing outside
#    it should contain a print() of its own.
#
#    Give each function a one-line docstring saying what it does.

# your function(s) go here


def status_of(percent):

    """Return the status based on the percentage."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"

def check (failed_logins, total_attempts):

    """Return the difference and percentage relative to the limit."""
    difference = failed_logins-total_attempts
    percent = (failed_logins/total_attempts)*100
    return difference, percent 

source_ip = input("Please insert a source:")                                      
failed_logins = float (input("Please insert the number of faild logines:"))       
total_attempts = float (input("Please insert the number of total attempts:"))

difference, percent = check(failed_logins, total_attempts)
status = status_of(percent)

def print_report(source_ip, failed_logins, total_attempts,difference, percent, status):
    
    """Print a formatted record report."""
print("=" * 34)
print(f"  RECORD CHECK - {source_ip}")
print("=" * 34)
print(f"  Failed logins : {failed_logins:>10.2f}")
print(f"  Total attempts: {total_attempts:>10.2f}")
print(f"  Difference    : {difference:>10.2f}")
print(f"  Percent       : {percent:>10.2f}%")
print(f"  Status        : {status:>10}")
print("=" * 34)
