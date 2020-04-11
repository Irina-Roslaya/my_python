from tkinter import *
window = Tk()
def read_list():
    import random
    import json    
    try:
        with open("dict.json") as f_obj:
            numbers = json.load(f_obj)
            dct = numbers[0]
        while dct:
            key = random.choice(list(dct.keys()))
            value = dct.pop(key)
        print(key)
    except Exception as e:
     print(e)
Label(window, text="Случайное слово:").grid(column=0, row=0)
Label(window, text="Укажите перевод слова:").grid(column=0, row=2)
ent=Entry(window,width=20)
ent.grid(column=0, row=3)
Button(text="Готово!",command=read_list).grid(row=5, column=0)
Button(text="Выход",command=exit).grid(row=6, column=0)
window.mainloop()