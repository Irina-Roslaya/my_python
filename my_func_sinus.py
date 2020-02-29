import math
element=input('Введите вещественное число: ')
if element:
    x=float(element)
    if 0.2<=x<=0.9:
        print(math.sin(x))
    else:
        print(1)
else:
    print('Введите вещественное число!')
        
