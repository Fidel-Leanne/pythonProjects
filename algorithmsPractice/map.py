li= [ 1,2,3,4,5,6,7,8,9,10]

def func(x):
    return x**x

#long way of doing it
newlist =[]
for i in li:
    newlist.append((func(i)))

print(newlist)

print(list(map(func,li)))