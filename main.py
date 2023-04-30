import time
from termcolor import colored

print ('''

█▀▀█ █▀▀ █▀▀█ █▀▀█ ▀▀█▀▀ █▀▀▄ █▀▀
█▄▄▀ █▀▀ █░░█ █░░█ ░░█░░ █░░█ █░░
▀░▀▀ ▀▀▀ █▀▀▀ ▀▀▀▀ ░░▀░░ ▀▀▀░ ▀▀▀

''')

print(colored('REPORT BOT DİSCORD İN PYTHON', 'red'))
time.sleep(1)
print ('''

[1]REPORT START     [3]INFORMATION

[2]EXİT             [4]CONTRIBUTORS

''')

input("CHOOSE AN OPTION:")

time.sleep(1)
input("ENTER A DISCORD URL:")

def send_report():
    
    print("Sending report...")

for i in range(1, 101):
    send_report()
    print(colored(f"Report {i} sent successfully", "green"))
    time.sleep(0.25)


print(colored("REPORT SENT SUCCESSFULLY, PLEASE CLOSE THE APP...", "red"))
