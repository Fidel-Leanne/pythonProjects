def func(x=1):
    return x**2

call = func()
print(call)

print(func(5))

def newFunction(word, frequency=1):
    print("The word is " + str(word)+ ". Their frequency is "+str(frequency)+" times.")
    print(word*frequency)

newFunction('tim',10)

def sum_numbers(*args):
    return sum(args)

print(sum_numbers(1, 2, 3, 4))  # Outputs: 10

#**kwargs: Used to pass a keyworded, variable-length argument list. 
# Inside the function, you can access them as a dictionary.
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="Alice", age=30)  
# Outputs:
# name: Alice
# age: 30
