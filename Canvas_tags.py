'''Теги'''
'''В отличие от идентификаторов, которые являются уникальными для каждого объекта,
один и тот же тег может присваиваться разным объектам. Дальнейшее обращение к такому
тегу позволит изменить все объекты, в которых он был указан. В примере ниже эллипс
и линия содержат один и тот же тег, а функция color изменяет цвет всех объектов с
тегом group1. Обратите внимание, что в отличие от имени идентификатора (переменная),
имя тега заключается в кавычки (строковое значение).'''
from tkinter import *

root = Tk()

c = Canvas(width=200, height=200, bg='white')
c.pack()

oval = c.create_oval(30, 10, 130, 80,tag='group1')
c.create_line(10, 100, 450, 100, tag='group1')

def color(event):
     c.itemconfig('group1', fill='red', width=3)

c.bind('<Button-3>', color)

root.mainloop()

'''Метод tag_bind() позволяет привязать событие (например, щелчок кнопкой мыши) к
определенной фигуре на Canvas. Таким образом, можно реализовать обращение к различным
областям холста с помощью одного и того же события. Пример ниже иллюстрирует, как
изменения на холсте зависят от того, где произведен клик.'''

from tkinter import *

c = Canvas(width=460, height=100, bg='grey80')
c.pack()

oval = c.create_oval(30, 10, 130, 80, fill='orange')
c.create_rectangle(180, 10, 280, 80, tag='rect', fill='lightgreen')
trian = c.create_polygon(330, 80, 380, 10, 430, 80, fill='white', outline='black')

def oval_func(event):
     c.delete(oval)
     c.create_text(80, 50, text='Круг')

def rect_func(event):
     c.delete('rect')
     c.create_text(230, 50, text='Прямоугольник')

def triangle(event):
     c.delete(trian)
     c.create_text(380, 50, text='Треугольник')

c.tag_bind(oval, '<Button-1>', oval_func)
c.tag_bind('rect', '<Button-1>', rect_func)
c.tag_bind(trian, '<Button-1>', triangle)

mainloop()

# Метод delete() удаляет объект. Если нужно очистить холст, то вместо идентификаторов
# или тегов используется константа ALL.
