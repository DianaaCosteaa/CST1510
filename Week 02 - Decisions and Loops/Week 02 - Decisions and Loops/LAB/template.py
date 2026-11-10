"""
RECORD CHECK  -  my version
===========================

Name  :  Diana Costea  
Lane  :  AI / Cyber / IT      (delete two)
Date  :  02/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

while True:
    source_ip = input("please insert a source ip, or 'quit': ")
    if source_ip == "quit":
        break

    failed_logines = float (input("Please insert the number of faild logines:"))
    total_attempts = float (input("Please insert the number of total attempts:"))

    difference = failed_logines-total_attempts                  #Run it with a total of 0 and note the error (do not fix it yet)
    percent = (failed_logines/total_attempts)*100               #ZeroDivisionError: division by zero

    if percent >= 100:
        status = ("over limit".upper())
    elif percent >=90:
        status =("Warning".upper()) 
    else:
        status =("ok".upper())

    print("=" * 34)
    print(f"Source IP:      {source_ip:>10}")
    print("=" * 34)

    print(f"Faild Login:    {failed_logines:>10.2f}")
    print(f"Total Attempts: {total_attempts:>10.2f}")
    print(f"Difference:     {difference:>+10.2f}")
    print(f"Percent:        {percent:>+10.2f}")
    print(f"Status:         {status:>10}")

    print("=" * 34)

