firstel = float(input("Введите значение первого элемента : "))
secondel = float(input("Введите значение второго элемента : "))
def my_max(firstel,secondel):
    if firstel > secondel:
        return firstel
    else:
        return secondel
    
print(my_max(firstel,secondel))
