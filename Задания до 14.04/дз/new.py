from tkinter import *
window = Tk()
Label(window, text="Температура в Цельсиях").grid(column=0, row=0)  
from operator import mul, add 
def celc_to_far():
    try:
        one=add(mul(9/5, int(ent.get())), 32)
        Lf.config(text = str(one))
    except ValueError:
        Lf.config(text = 'Ошибка ввода')
ent=Entry(window,width=20)
ent.grid(column=0, row=1)
Lf=Label(window)
Lf.grid(column=0, row=3)
Button(text="Конвертировать", command = celc_to_far).grid(row=2, column=0)
Button(text="Выход",command=exit).grid(row=4, column=0)
window.mainloop()