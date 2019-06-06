'''Теги'''
'''Особенностью текстового поля библиотеки Tk является возможность форматировать
текст в нем, то есть придавать его разным частям разное оформление. Делается это
с помощью методов tag_add() и tag_config(). Первый добавляет тег, при этом надо
указать его произвольное имя и отрезок текста, к которому он будет применяться.
Метод tag_config() настраивает тегу стили оформления.'''
from tkinter import *
root = Tk()

text = Text(width=50, height=10)
text.pack()
text.insert(1.0, "Hello world!\nline two")

text.tag_add('title', 1.0, '1.end')
text.tag_config('title', font=("Verdana", 24, 'bold'), justify=CENTER)

root.mainloop()

'''Вставка виджетов в текстовое поле'''
# В Text можно вставлять другие виджеты помощью метода window_creat().
# Потребность в этом не велика, однако может быть интересна с объектами типа Canvas.
# Данный класс будет изучен позже. В примере ниже вставляется метка в текущую (INSERT)
# позицию курсора.
from tkinter import *

def smile():
    label = Label(text=":)", bg="yellow")
    text.window_create(INSERT, window=label)

root = Tk()

text = Text(width=50, height=10)
text.pack()

button = Button(text=":)", command=smile)
button.pack()

root.mainloop()
# Размещение метки в функции позволяет каждый раз при вызове функции создавать
# новую метку. Иначе, если бы метка была в основной ветке программы, предыдущая исчезала бы.
