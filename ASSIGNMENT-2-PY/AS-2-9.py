import re
email = input("Enter an email address: ")
if re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
    print("Valid email address")
else:
    print("Invalid email address")
