'''Можно подвязывать дочерние меню к filemenu и helpmenu, создавая многоуровневые
списки пунктов меню.'''

from tkinter import *

root = Tk()

mainmenu = Menu(root)
root.config(menu = mainmenu)

filemenu = Menu(mainmenu, tearoff = 0)
filemenu.add_command(label = 'Открыть...')
filemenu.add_command(label = 'Новый')
filemenu.add_command(label = 'Сохранить...')
filemenu.add_command(label = 'Выход')

helpmenu = Menu(mainmenu, tearoff = 0)

helpmenu2 = Menu(helpmenu, tearoff = 0)
helpmenu2.add_command(label = 'Локальная справка')
helpmenu2.add_command(label = 'На сайте')

helpmenu.add_cascade(label = 'Помощь', menu = helpmenu2)
helpmenu.add_command(label = 'О программе')

mainmenu.add_cascade(label = 'Файл', menu = filemenu)
mainmenu.add_cascade(label = 'Справка', menu = helpmenu)

root.mainloop()

'''Метод add_separator() добавляет линию разделитель в меню. Используется для
визуального разделения групп команд.

В tkinter можно создать всплывающее меню, оно же контекстное (если настроить его
появление по клику правой кнопкой мыши). Для этого экземпляр меню подвязывается
не через опцию menu к родительскому виджету, а к меню применяется метод post(),
аргументами которого являются координаты того места, где должно появляться меню.'''

from tkinter import *

def circle():
    c.create_oval(x, y, x + 30, y + 30)

def square():
    c.create_rectangle(x, y, x + 30, y + 30)

def triangle():
    c.create_polygon(x, y, x - 15, y + 30, x + 15, y + 30, fill = 'white', outline = 'black')    # закрашивают треугольник

def popup(event):
    global x, y
    x = event.x
    y = event.y
    menu.post(event.x_root, event.y_root)

root = Tk()

c = Canvas(width = 300, height = 300, bg = 'white')
c.pack()

menu = Menu(tearoff = 0)
menu.add_command(label = 'Круг', command = circle)
menu.add_command(label = 'Квадрат', command = square)
menu.add_command(label = 'Треугольник', command = triangle)

x = 0
y = 0

c.bind('<Button-3>', popup)

root.mainloop()
