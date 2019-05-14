'''В Tkinter существует три так называемых менеджера геометрии – упаковщик,
сетка и размещение по координатам. Рассмотрим первый как
наиболее простой и часто используемый, остальные два упомянем позже.'''
# Упаковщик (packer) вызывается методом pack(), который имеется у всех
# виджетов-объектов. Если к элементу интерфейса не применить какой-либо из
# менеджеров геометрии, то он не отобразится в окне. При этом в одном окне
# (или любом другом родительском виджете) нельзя комбинировать разные менеджеры.
# Если вы начали размещать виджеты методом pack(), то не надо тут же использовать
# методы grid() (сетка) и place() (место).
# Если в упаковщики не передавать аргументы, то виджеты будут располагаться
# вертикально, друг над другом. Тот объект, который первым вызовет pack(), будет
# вверху. Который вторым – под первым, и так далее.
'''У метода pack() есть параметр side (сторона), который принимает одно из
четырех значений-констант tkinter – TOP, BOTTOM, LEFT, RIGHT (верх, низ, лево,
право). По умолчанию, когда в pack() не указывается side, его значение
равняется TOP. Из-за этого виджеты располагаются вертикально.'''

from tkinter import *

root = Tk()

l1 = Label(width = 7, height = 4, bg = 'yellow', text = "1")
l2 = Label(width = 7, height = 4, bg = 'orange', text = "2")
l3 = Label(width = 7, height = 4, bg = 'lightgreen', text = "3")
l4 = Label(width = 7, height = 4, bg = 'lightblue', text = "4")

'''Рассмотрим разные комбинации значений сайда:'''
# С верху в низ
l1.pack()
l2.pack()
l3.pack()
l4.pack()

# Снизу вверху
# l1.pack(side  =  BOTTOM)
# l2.pack(side  =  BOTTOM)
# l3.pack(side  =  BOTTOM)
# l4.pack(side  =  BOTTOM)

# Слева на право
# l1.pack(side  =  LEFT)
# l2.pack(side  =  LEFT)
# l3.pack(side  =  LEFT)
# l4.pack(side  =  LEFT)

# Справа на лево
# l1.pack(side  =  RIGHT)
# l2.pack(side  =  RIGHT)
# l3.pack(side  =  RIGHT)
# l4.pack(side  =  RIGHT)

# Крестом
# l1.pack(side  =  TOP)
# l2.pack(side  =  BOTTOM)
# l3.pack(side  =  RIGHT)
# l4.pack(side  =  LEFT)

root.mainloop()

'''Проблема последнего варианта в том, что если надо разместить виджеты квадратом,
т. е. два сверху, два снизу ровно под двумя верхними, то сделать это проблематично,
если вообще возможно. Поэтому прибегают к вспомогательному виджету – фрейму (рамке),
который порождается от класса Frame.'''
# Фреймы размещают на главном окне, а уже в фреймах – виджеты:

from tkinter import *

root = Tk()
f_top = Frame(root)    # root можно не указывать
f_bot = Frame(root)
# Кроме Frame существует похожий класс LabelFrame – фрейм с подписью. В отличие
# от простого фрейма у него есть свойство text.
# f_top = LabelFrame(text="Верх")
# f_bot = LabelFrame(text="Низ")

l1 = Label(f_top, width = 7, height = 4, bg = 'yellow', text = "1")
l2 = Label(f_top, width = 7, height = 4, bg = 'orange', text = "2")
l3 = Label(f_bot, width = 7, height = 4, bg = 'lightgreen', text = "3")
l4 = Label(f_bot, width = 7, height = 4, bg = 'lightblue', text = "4")

f_top.pack(padx = 10, pady = 10)
f_bot.pack(padx = 10, pady = 10)
# у метода pack есть padx = 10, pady = 10 - внешний отступ, ipadx = 10, ipady = 10 - внутренний отступ
l1.pack(side = LEFT)
l2.pack(side = LEFT)
l3.pack(side = LEFT)
l4.pack(side = LEFT)

root.mainloop()
