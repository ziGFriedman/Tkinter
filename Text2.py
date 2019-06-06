'''Основные методы у Text такие же как у Entry – get(), insert(), delete(). Однако,
если в случае однострочного текстового поля было достаточно указать один индекс
элемента при вставке или удалении, то в случае многострочного надо указывать
два – номер строки и номер символа в этой строке (другими словами, номер столбца).
При этом нумерация строк начинается с единицы, а столбцов – с нуля.'''
from tkinter import *

def insertText():
    s = "Hello World"
    text.insert(1.0, s)

def getText():
    s = text.get(1.0, END)
    label['text'] = s

def deleteText():
    text.delete(1.0, END)

root = Tk()

text = Text(width=25, height=5)
text.pack()

frame = Frame()
frame.pack()

b_insert = Button(frame, text="Вставить", command=insertText)
b_insert.pack(side=LEFT)

b_get = Button(frame, text="Взять", command=getText)
b_get.pack(side=LEFT)

b_delete = Button(frame, text="Удалить", command=deleteText)
b_delete.pack(side=LEFT)

label = Label()
label.pack()

root.mainloop()

# Методы get() и delete() могут принимать не два, а один аргумент. В таком случае
# будет обрабатываться только один символ в указанной позиции.
