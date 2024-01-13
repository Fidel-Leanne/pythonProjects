while True:
    try: 
        x= int(input('enter int'))
    except ValueError:
        pass
    else:
        break

print(f'x is {x}')