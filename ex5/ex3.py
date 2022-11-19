
print('#>---------------------<MENU>---------------------<#')
print('|  h - The total amount of the order               |')
print('|  s - Cost of one set-top box including discount  |')
print('#>------------------------------------------------<#')

try:
    a = int(input("Price?:  "))
    if a < 0:
        print("Error: Bro, We don't take no Negative Numbers around here.")
        exit()
    b = int(input("Procent of discount?:  "))
    if b < 0:
        print("Error: Bro, We don't take no Negative Numbers around here.")
        exit()  
    c = int(input("How many?:  "))
    if c < 0:
        print("Error: Bro, We don't take no Negative Numbers around here.")
        exit()
    

    action = input('action->')
    if action == "h":
            res = ((a * c) - (a * c) * (b * 0.01))
            print ("Ur result" + " " + str(res))
    elif action == "s":
            res = (a - (a * (b * 0.01)))
            print ("Ur result" + " " + str(res))

except ValueError as vl_ex:
    print(f'Value error: {vl_ex}')
except RecursionError as err:
    print('Error: ', str(err))
except AssertionError :
    print("Number is negative")