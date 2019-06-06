'''Заголовок окна'''
'''По умолчанию с стоке заголовка окна находится надпись "tk". Для установки
собственного названия используется метод title().'''
# …
# root.title("Главное окно")
# …

'''Если необходимо, заголовок окна можно вообще убрать. В программе ниже второе окно
(Toplevel) открывается при клике на кнопку, оно не имеет заголовка, так как к нему
был применен метод overrideredirect() с аргументом True. Через пять секунд данное
окно закрывается методом destroy().'''

from tkinter import *

root = Tk()

root.title("Главное окно")

def about():
    a = Toplevel()
    a.geometry('200x150')
    a['bg'] = 'grey'
    a.overrideredirect(True)
    Label(a, text="About this").pack(expand=1)
    a.after(5000, lambda: a.destroy())

Button(text="Button", width=20).pack()
Label(text="Label", width=20, height=3).pack()
Button(text="About", width=20, command=about).pack()

root.mainloop()
