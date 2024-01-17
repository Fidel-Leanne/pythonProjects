names=[] 

with open('names.txt') as f:
    for line in f:
        names.append(line.rstrip())

for name in names:
    print(f'hello {name}')
