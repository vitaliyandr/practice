try:
    a = int(input("Size in gb-> "))
    if a < 0:
       raise Exception('Negative number!')
    b = int(input("Speed-> "))
    if b < 0:
       raise Exception('Negative number!')
    
    print('#>---------<MENU>---------<#')
    print('|        h - Hour          |')
    print('|        m - Minutes       |')
    print('|        s - Seconds       |')
    print('#>------------------------<#')

    action = input("action->")
    if action == "h":
        res = ((a * 8589934592) / b) / 3600
        print("Ur result", str(res))
    elif action == "m":
        res = ((a * 8589934592) / b) / 60
        print("Ur result", str(res))
    elif action == "s":
        res = (a * 8589934592) / b
        print("Ur result", str(res))
    else:
        print("Error!")

except ValueError as vl_ex:
    print(f'Value error: {vl_ex}')
except Exception as ex:
    print(f'Error: {ex}')
    print(f'Name: {ex.__class__.__name__}')