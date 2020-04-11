from tkinter import *
window = Tk()
Lf=Label(window)
Lf.grid(column=0, row=1)
def true():
    import random
    import json    
    try:
        with open("dict.json",encoding='utf8') as f_obj:
            numbers = json.load(f_obj)
        dct = numbers[0]
        while dct:
            key = random.choice(list(dct.keys()))
            value = dct.pop(key) 
        Lf.config(text = key)           
    except Exception as e:
        print(e)
    return value
def res():
    value=true()
    if str(ent.get())==value:
        f.config(text = 'Угадали!')
    else:
        f.config(text = 'Не угадали :(')
f=Label(window)
f.grid(column=0, row=4)
Label(window, text="Случайное слово:").grid(column=0, row=0)
Label(window, text="Укажите перевод слова:").grid(column=0, row=2)
ent=Entry(window,width=20)
ent.grid(column=0, row=3)
Button(text="Готово!",command =res).grid(row=5, column=0)
Button(text="Выход",command=exit).grid(row=6, column=0)
window.mainloop()