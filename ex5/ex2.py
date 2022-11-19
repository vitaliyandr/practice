from math import pi 
try:
    d = float(input('Enter the circles diameter in cm:'))
    if d < 0 or d == 0:
        print('D cant be negative!')
    elif d > 0:
         action = input('Enter what would u to do(S L)')
    if action == 'S':
         res = round((1/4) * pi * d**2)
         print('\nThe circles area is about {res} cm\u00b2.'.format(res=res))
    elif action == 'L':
         res = round((2*pi)*0.5*d)
         print(res)
    else:
         print('Error!')
except ValueError as vl_ex:
    print(f'Value error: {vl_ex}')
except Exception as ex:
    print(f'Error: {ex}')
