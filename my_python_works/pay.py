hours = int(input("Количество отработанных часов: "))
pay_rate = int(input("Почасовая ставка оплаты труда: "))
def pay(hours,pay_rate):
    return hours * pay_rate
print(pay(hours,pay_rate))
