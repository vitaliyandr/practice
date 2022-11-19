try:
    a = int(input("Type number-> "))
    if a >= 0 and a < 6 or a == 24:
        print("Good night")
    elif a >= 6 and a < 13:
        print("Good morning")
    elif a >= 13 and a < 17:
        print("Good Day")
    elif a >= 17 and a < 24:
        print("Good evening")
    else:
        print("ERROR")
except ValueError as vl_ex:
    print(f'Value error: {vl_ex}')
except Exception as ex:
    print(f'Error: {ex}')
    print(f'Name: {ex.__class__.__name__}')

