from tkinter import *
listt=[]
list2=[]
list3=[]
newdict={}
def save_inp():
    i=0
    listt.append(["Task: ",f'{inp.get()}'])
    listt.append(["Category: ",f'{inp2.get()}'])
    listt.append(["Time: ",f'{inp3.get()}'])
    while len(list2)*3 != len(listt):
        newdict=dict(listt[i:])
        list2.append(newdict)
        i+=3
    import json    
    with open("tasks2.json", 'w') as f_obj:
        json.dump(list2, f_obj)
def show(): 
    list3=[' '.join(i) for i in listt]
    print("\n".join(list3))   
window = Tk()
window.title("Менеджер задач")
window.geometry('220x150')  
Label(window, text="Задача:").grid(column=0, row=0) 
inp = StringVar()  
inp2= StringVar()
inp3= StringVar()
Entry(window,width=20, textvariable = inp).grid(column=1, row=0) 
Label(window, text="Категория: ").grid(column=0, row=1) 
Entry(window,width=20,textvariable = inp2).grid(column=1, row=1)
Label(window, text="Время: ").grid(column=0, row=2) 
Entry(window,width=20,textvariable = inp3).grid(column=1, row=2)
Button(text="Заказать", command = save_inp).grid(row=3, column=1)
Button(text="Список задач",command=show).grid(row=4, column=1)
Button(text="Выход",command=exit).grid(row=5, column=1)
window.mainloop()