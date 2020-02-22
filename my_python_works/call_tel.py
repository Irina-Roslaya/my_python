code = int(input("Введите код города: "))
time = int(input("Введите значение, соответствующее длительности переговоров (в минутах): "))
def cost(c,t):
    if c == 343:
        return t*15 
    elif c == 381:
        return t*18 
    elif c == 473:
        return t*13 
    elif c == 485:
        return t*11 
    else:
        return "Нет данных о цене одной минуты переговоров"

print(cost(code,time))
