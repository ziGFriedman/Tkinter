'''Реализуем в программе объектно-ориентированный подход.'''

from tkinter import *

class Block:
    def __init__(self, master):
        self.e = Entry(master, width = 20)
        self.b = Button(master, text = "Преобразовать")
        self.l = Label(master, bg = 'black', fg = 'white', width = 20)
        self.e.pack()
        self.b.pack()
        self.l.pack()

    def setFunc(self, func):
        '''Функция-обработчик события нажатия на кнопку устанавливается не с помощью
        метода bind(), а с помощью свойства кнопки 'command'. В этом случае в вызываемой
        функции (в данном случае это метод) не требуется параметр event. В метод мы
        передаем только сам объект.'''
        self.b['command'] = eval('self.' + func)
        
# Функция eval() преобразует строку в исполняемый код. В результате получается self.b['command'] = self.strToSortlist или self.b['command'] = self.strReverse.

    def strToSortlist(self):
        s = self.e.get()
        s = s.split()
        s.sort()
        self.l['text'] = ' '.join(s)

    def strReverse(self):
        s = self.e.get()
        s = s.split()
        s.reverse()
        self.l['text'] = ' '.join(s)

'''Пусть комплект из метки, кнопки и поля представляет собой один объект,
порождаемый от некого класса, скажем, Block. Тогда в основной ветке программы
будет главное окно, объект типа Block и запуск окна. Поскольку блок должен
быть привязан к главному окну, то неплохо бы передать в конструктор класса
окно-родитель:'''

root = Tk()

first_block = Block(root)
first_block.setFunc('strToSortlist')

second_block = Block(root)
second_block.setFunc('strReverse')

root.mainloop()
