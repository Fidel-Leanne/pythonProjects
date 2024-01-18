import re

name= input('Whats your username').strip()

re.search(r'^\S.()')

if ',' in name:
    last, first= name.split(',')
    name= f'{first}, {last}'

print(f'hello {name}')