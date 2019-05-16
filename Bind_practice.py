'''Напишите программу по следующему описанию. Нажатие Enter в однострочном текстовом
поле приводит к перемещению текста из него в список (экземпляр Listbox). При двойном
клике (<Double-Button-1>) по элементу-строке списка, она должна копироваться в
текстовое поле.'''
from tkinter import *

root = Tk()

def to_lb(event):
    lb.insert(END, ent.get())
    ent.delete(0, END)

def to_ent(event):
    select = lb.get(lb.curselection())
    ent.delete(0, END)
    ent.insert(0, select)

ent = Entry()
ent.bind('<Return>', to_lb)
ent.pack()

lb = Listbox()
lb.bind('<Double-Button-1>', to_ent)
lb.pack()

root.mainloop()
