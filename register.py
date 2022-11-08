import time
import pyfiglet as pfg


print(pfg.figlet_format("BMM", width=50))
print('Bulk----Music----Mail\n\n')
name = input(f"[+] What is your name (full): ")
email = input(f"[+] What is your email address: ")
print("Processing...")
with open("list.txt","a") as list:
    list.write(f"\n{name} - {email}")
time.sleep(4)
print("Thanks for subscribing to our service.")
