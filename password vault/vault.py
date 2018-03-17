import getpass
import time

# Make sure to replace all the passwords with yours.

USERNAME = "admin"
PASSWORD = "admin"

print("Hello", getpass.getuser())
AUTH = str(input("Username: "))
AUTH2 = str(input("Password: "))

if AUTH == USERNAME and AUTH2 == PASSWORD:
    print("Github: (my password)")
    print("Paypal: (my password)")
    print("Email: (my password)")
    time.sleep(10)
else:
    print("Incorrect username or password!")
    time.sleep(3)