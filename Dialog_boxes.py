'''Пакет tkinter содержит несколько модулей, предоставляющих доступ к уже готовым
диалоговым окнам. Это окна различных сообщений, выбора по принципу "да-нет", открытия
и сохранения файлов и др. В этом уроке рассмотрим примеры окон из модулей messagebox
и filedialog пакета tkinter.

Модули пакета необходимо импортировать отдельно. То есть вы импортируете содержимое
tkinter (например, from tkinter import *) и отдельно входящий в состав пакета tkinter
модуль:
import tkinter.messagebox → tkinter.messagebox.askyesno()
from tkinter.messagebox import * → askyesno()
from tkinter import messagebox → messagebox.askyesno()
from tkinter import messagebox as mb (вместо mb может быть любой идентификатор) → mb.askyesno()'''

'''Модуль messagebox – стандартные диалоговые окна
Окно выбора "да" или "нет" – askyesno():'''

from tkinter import *
from tkinter import messagebox as mb

def check():
    answer = mb.askyesno(title = 'Вопрос', message = 'Перенести данные?')
    if answer == True:
        s = entry.get()
        entry.delete(0, END)
        label['text'] = s

root = Tk()
entry = Entry()
entry.pack(pady=10)
Button(text = 'Передать', command = check).pack()
label = Label(height = 3)
label.pack()

root.mainloop()

'''Нажатие "Да" в диалоговом окне возвращает в программу True, "Нет" вернет False
(также как закрытие окна через крестик). Таким образом в коде можно обработать выбор
пользователя. В данном случае если последний соглашается, то данные переносятся из
поля в метку.

Опции title и message являются позиционными, так что можно указывать только
значения: askyesno("Вопрос", "Перенести данные?").'''

'''Подобные окна генерируются при использовании функции askokcancel() с надписями на
кнопках "ОК" и "Отмена", askquestion() (возвращает не True или False, а строки 'yes'
или 'no'), askretrycancel() ("Повторить", "Отмена"), askyesnocancel() ("Да", "Нет",
"Отмена").'''

'''Другую группу составляют окна с одной кнопкой, которые служат для вывода сообщений
различного характера. Это showerror(), showinfo() и showwarning().'''
# …
# def check():
#     s = entry.get()
#     if s.isdigit() == False:
#         mb.showerror('Ошибка', 'Должно быть введено число')
#     else:
#         entry.delete(0, END)
#         label['text'] = s
# … 
