'''Модуль filedialog – диалоговые окна открытия и сохранения файлов'''
'''Рассмотрим две функции из модуля filedialog – askopenfilename() и asksaveasfilename().
Первая предоставляет диалоговое окно для открытия файла, вторая – для сохранения. Обе
возвращают имя файла, который должен быть открыт или сохранен, но сами они его не открывают
и не сохраняют. Делать это уже надо программными средствами самого Python.'''

from tkinter import *
from tkinter import filedialog as fd

def insertText():
    file_name = fd.askopenfilename()
    f = open(file_name)
    s = f.read()
    text.insert(1.0, s)
    f.close()

def extractText():
    file_name = fd.asksaveasfilename(filetypes=(('TXT files', '*.txt'), (
        'HTML files', '*.html;*.htm'), ('All files', '*.*')))
    f = open(file_name, 'w')
    s = text.get(1.0, END)
    f.write(s)
    f.close()

root = Tk()
text = Text(width=50, height=25)
text.grid(columnspan=2)

b1 = Button(text='Открыть', command=insertText)
b1.grid(row=1, sticky=E)
b2 = Button(text='Сохранить', command=extractText)
b2.grid(row=1, column=1, sticky=W)

root.mainloop()

'''Опция filetype позволяет перечислить типы файлов, которые будут сохраняться
или открываться, и их расширения.

Примечание. В приведенном коде при размещении текстового поля методом grid() не
указаны аргументы row и column. В таких случаях подразумевается, что их значениями
являются нули.'''
