'''В приведенной в уроке программе с функциями askopenfilename() и asksaveasfilename()
генерируются исключения, если диалоговые окна были закрыты без выбора или указания
имени файлов.

Напишите код обработки данных исключений. При этом для пользователя должно появляться
информационное диалоговое окно с сообщением о том, что файл не загружен или не сохранен.

Добавьте кнопку 'Очистить', которая удаляет текст из поля. Перед удалением пользователь
должен подтвердить свои намерения через соответствующее диалоговое окно.'''

from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog as fd

def insert_text():
    try:
        file_name = fd.askopenfilename()
        f = open(file_name)
        s = f.read()
        text.insert(1.0,s)
        f.close()
    except FileNotFoundError:
        mb.showinfo('Внимание', 'Файл не загружен')

def extract_text():
    try:
        file_name = fd.asksaveasfilename(filetypes=(('TXT files', '*.txt'), (
            'HTML files', '*.html; *.htm'), ('All files', '*.*')))
        f = open(file_name, 'w')
        s = text.get(1.0, END)
        f.write(s)
        f.close()
    except FileNotFoundError:
        mb.showinfo('Внимание', 'Файл не сохранён')

def delete_text():
    answer = mb.askyesno('Подтверждение', message='Вы хотите удалить текст?')
    if answer == True:
        text.delete(0.0, END)

root = Tk()
text = Text(width=50, height=25)
text.grid(columnspan=2)

Button(text='Открыть', command=insert_text).grid(row=1, sticky=E)
Button(text='Сохранить', command=extract_text).grid(row=1, column=1, sticky=W)
Button(text='Очистить', command=delete_text).grid(row=1, column=1)

root.mainloop()
