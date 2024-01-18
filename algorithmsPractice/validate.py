import re

email_address = input('Email Address \n').strip()

if re.search(r'^\S\w+@\w+\.havard+\.com', email_address, re.IGNORECASE):
    print('valid email address')
else:
    print('Invalid email address')