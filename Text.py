'''Text – многострочное текстовое поле'''
# В tkinter многострочное текстовое поле создается от класса Text. По умолчанию
# его размер равен 80-ти знакоместам по горизонтали и 24-м по вертикали.
# Однако эти свойства можно изменять с помощью опций width и height. Есть возможность
# конфигурировать шрифт, цвета и другое.
from tkinter import *

root = Tk()

# Значение WORD опции wrap позволяет переносить слова на новую строку целиком, а не по буквам.
text = Text(width=25, height=5, bg="darkgreen", fg='white', wrap=WORD)

text.pack()
root.mainloop()

'''Text и Scrollbar'''
# В tkinter скроллеры производятся от класса Scrollbar. Объект-скроллер связывают с
# виджетом, которому он требуется. Это не обязательно многострочное текстовое поле.
# Часто полосы прокрутки бывают нужны спискам, которые будут рассмотрены позже.
from tkinter import *

root = Tk()

text = Text(width=20, height=7)
text.pack(side=LEFT)

scroll = Scrollbar(command=text.yview)
scroll.pack(side=LEFT, fill=Y)

text.config(yscrollcommand=scroll.set)

root.mainloop()
# Здесь создается скроллер, к которому с помощью опции command привязывается прокрутка
# текстового поля по оси y – text.yview. В свою очередь текстовому полю опцией
# yscrollcommand устанавливается ранее созданный скроллер – scroll.set.
