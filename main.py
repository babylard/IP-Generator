import subprocess
from time import sleep
from tkinter import Y

question = input("Would you like to generate a new IP for all interfaces? (y/n): ")
    
if question == 'y':
    print("Note: Output lines may appear!")

    sleep(5)

    subprocess.call("ipconfig /release", shell=True)
    subprocess.call("ipconfig /renew", shell=True)
    print("-")
    print("-")
    print("-")
    print("-")
    print("New IPs have been generated! Closing window in 5 seconds.")
    print("-")
    print("-")
    print("-")
    print("-")
    sleep(5)

else:
    print("You may now safely close this window.")