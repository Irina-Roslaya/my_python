element = int(input("Введите число: "))
def even_q(element):
    if element % 2 == 0:
        return "Число четное"
    else:
        return "Число нечетное"
print(even_q(element))
