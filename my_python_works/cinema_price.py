film = input("Выбрать фильм: ")
date = input("Выбрать день (сегодня, завтра): ")
time = int(input("Выбрать время: "))
amount = int(input("Выбрать количество билетов: "))
if film == 'Паразиты':
    if  date == 'завтра':
        if time == 12:
            cost = 250
            if amount >= 20:
                print (cost*amount - cost*amount*0.25)
            else:
                print (cost*amount - cost*amount*0.05)
        elif time == 16:
            cost = 350
            if amount >= 20:
                print (cost*amount - cost*amount*0.25)
            else:
                print (cost*amount - cost*amount*0.05)
        elif time == 20:
             cost = 450
             if amount >= 20:
                print (cost*amount - cost*amount*0.25)
             else:
                print (cost*amount - cost*amount*0.05)
    else:
        if time == 12:
             cost = 250
             if amount >= 20:
                print (cost*amount - cost*amount*0.20)
             else:
                print (cost*amount)
        elif time == 16:
            cost = 350
            if amount >= 20:
                print (cost*amount - cost*amount*0.20)
            else:
                print (cost*amount)
        elif time == 20:
            cost = 450
            if amount >= 20:
                print (cost*amount - cost*amount*0.20)
            else:
                print (cost*amount)
            if amount >= 20:
                print (cost*amount - cost*amount*0.20)
            else:
                print (cost*amount)
elif film == '1917':
    if  date == 'завтра':
        if time == 10:
            cost = 250
            if amount >= 20:
                print (cost*amount - cost*amount*0.25)
            else:
                print (cost*amount - cost*amount*0.05)
        elif time == 13:
            cost = 350
            if amount >= 20:
                print (cost*amount - cost*amount*0.25)
            else:
                print (cost*amount - cost*amount*0.05)
        elif time == 16:
            cost = 350
            if amount >= 20:
                print (cost*amount - cost*amount*0.25)
            else:
                print (cost*amount - cost*amount*0.05)
    else:
        if time == 10:
            cost = 250
            if amount >= 20:
                print (cost*amount - cost*amount*0.20)
            else:
                print (cost*amount)
        elif time == 13:
            cost = 350
            if amount >= 20:
                print (cost*amount - cost*amount*0.20)
            else:
                print (cost*amount)
        elif time == 16:
            cost = 350
            if amount >= 20:
                print (cost*amount - cost*amount*0.20)
            else:
                print (cost*amount)
elif film == 'Соник в кино':
    if  date == 'завтра':
        if time == 10:
            cost = 350
            if amount >= 20:
                print (cost*amount - cost*amount*0.25)
            else:
                print (cost*amount - cost*amount*0.05)
        elif time == 15:
            cost = 450
            if amount >= 20:
                print (cost*amount - cost*amount*0.25)
            else:
                print (cost*amount - cost*amount*0.05)
        elif time == 18:
            cost = 450
            if amount >= 20:
                print (cost*amount - cost*amount*0.25)
            else:
                print (cost*amount - cost*amount*0.05)
    else:
        if time == 10:
            cost = 350
            if amount >= 20:
                print (cost*amount - cost*amount*0.20)
            else:
                print (cost*amount)
        elif time == 15:
            cost = 450
            if amount >= 20:
                print (cost*amount - cost*amount*0.20)
            else:
                print (cost*amount)
        elif time == 18:
            cost = 450
            if amount >= 20:
                print (cost*amount - cost*amount*0.20)
            else:
                print (cost*amount)
                            
                
            
                

