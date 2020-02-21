element = input("Введите атомный номер : ")
if element:
    number = float(element)
    if number == 3:
        print("Литий")
    elif number == 25:
        print("Марганец")
    elif number == 80:
        print("Ртуть")
    elif number == 17:
        print("Хлор")
    else:
        print("Нет информаци о данном элементе")
else:
    print("Введите атомный номер !")
