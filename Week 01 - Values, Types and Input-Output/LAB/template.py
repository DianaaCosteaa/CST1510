"""
RECORD CHECK  -  my version
===========================

Name  : Diana Costea 
Lane  : Cyber Security 
Date  : 25/09/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
# 1. Ask the user for your three values.
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())
#
#    Remember: input() always gives back text.


source_ip = input("please insert the Source IP: ")
failed_login = float(input("Please insert the number of Feiled Logins: "))
total_attempts = float (input("Please insert yhe number of Total Attempts: "))



# ================================================================== PROCESS
# 2. Work out what you were NOT given.       [Typical and above]
#
#    - difference : how far the first is from the second
#    - percent    : the first as a percentage of the second

difference = failed_login-total_attempts   
percent = (failed_login/total_attempts)*100      


# =================================================================== OUTPUT
# 3. Print the report.
#    Difference always shows its sign, plus one line of your own
#
#    Useful:   f"{value:>10.2f}"    right-aligned, 2 decimal places
#              f"{value:>+10.2f}"   the same, but always shows the sign
print("=" * 34)
print(f"Source IP:      {source_ip:>10}")
print("=" * 34)

print(f"Faild Login:    {failed_login:>10.2f}")
print(f"Total Attempts: {total_attempts:>10.2f}")
print(f"Difference:     {difference:>+10.2f}")
print(f"Percent:        {percent:>10.2f}")

print("=" * 34)

