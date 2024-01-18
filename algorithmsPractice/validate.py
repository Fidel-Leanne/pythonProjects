import re

email_address = input('Email Address \n').strip()

if re.search(r'^\S\w+@\w+\.com', email_address):
    print('valid email address')
else:
    print('Invalid email address')