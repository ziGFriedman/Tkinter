'''В Tkinter от класса Radiobutton создаются радиокнопки, от класса Checkbutton – флажки.'''
# Экземпляры Checkbutton также могут быть визуально оформлены в группу, но каждый флажок
# независим от остальных. Каждый может быть в состоянии "установлен" или "снят", независимо
# от состояний других флажков. Другими словами, в группе Checkbutton можно сделать
# множественный выбор, в группе Radiobutton – нет.
'''Связь двух радиокнопок устанавливается через общую переменную, разные значения которой
соответствуют включению разных радиокнопок группы. У всех кнопок одной группы свойство
variable устанавливается в одно и то же значение – связанную с группой переменную. А
свойству value присваиваются разные значения этой переменной.'''
# В Tkinter нельзя использовать любую переменную для хранения состояний виджетов. Для этих
# целей предусмотрены специальные классы-переменные пакета tkinter – BooleanVar, IntVar,
# DoubleVar, StringVar. Первый класс позволяет принимать своим экземплярам только булевы
# значения (0 или 1 и True или False), второй – целые, третий – дробные, четвертый – строковые.
from tkinter import *

def change():
    if var.get() == 0:
        label['bg'] = 'red'
    elif var.get() == 1:
        label['bg'] = 'green'
    elif var.get() == 2:
        label['bg'] = 'blue'

root = Tk()

var = IntVar()
var.set(0)

red = Radiobutton(text="Red", variable=var, value=0)
green = Radiobutton(text="Green", variable=var, value=1)
blue = Radiobutton(text="Blue", variable=var, value=2)

button = Button(text="Изменить", command=change)
label = Label(width=20, height=10)

red.pack()
green.pack()
blue.pack()
button.pack()
label.pack()

root.mainloop()
