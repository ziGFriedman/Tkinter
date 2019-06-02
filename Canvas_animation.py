'''Практическая работа. Анимация в tkinter'''
'''В данной программе создается анимация круга, который движется от левой границы
холста до правой:'''
from tkinter import *

root = Tk()
c = Canvas(root, width = 300, height=200, bg='white')
c.pack()

ball = c.create_oval(0, 100, 40, 140, fill='green')

def motion():
    c.move(ball, 1, 0)
    if c.coords(ball)[2] < 300:
        root.after(10, motion)

motion()

root.mainloop()

'''Выражение c.coords(ball) возвращает список текущих координат объекта (в данном
случае это ball). Третий элемент списка соответствует его второй координате x.
Метод after() вызывает функцию, переданную вторым аргументом, через количество
миллисекунд, указанных первым аргументом.'''

'''Изучите приведенную программу и самостоятельно запрограммируйте постепенное движение
фигуры в ту точку холста, где пользователь кликает левой кнопкой мыши. Координаты
события хранятся в его атрибутах x и y (event.x, event.y).'''

from tkinter import *

root = Tk()

root.title('Мяч догоняет мышь')
c = Canvas(root, width=300, height=200, bg='white')
c.pack()

ball = c.create_oval(0, 100, 20, 120, fill='green')

def mouse(event):
    x = event.x
    y = event.y
    root.unbind('<Button-1>')
    move(x, y)

def move(x, y):
    if (c.coords(ball)[2] + c.coords(ball)[0]) / 2 < x:
        c.move(ball, 1, 0)
    if (c.coords(ball)[2] + c.coords(ball)[0]) / 2 > x:
        c.move(ball, -1, 0)
    if (c.coords(ball)[3] + c.coords(ball)[1]) / 2 < y:
        c.move(ball, 0, 1)
    if (c.coords(ball)[3] + c.coords(ball)[1]) / 2 > y:
        c.move(ball, 0, -1)
    if (c.coords(ball)[3] + c.coords(ball)[1]) / 2 != y or (
        c.coords(ball)[2] + c.coords(ball)[0]) / 2 != x :
        root.after(10, move, x, y)
    else:
        root.bind('<Button-1>', mouse)

root.bind('<Button-1>', mouse)

root.mainloop()
