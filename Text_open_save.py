'''Напишите программу, состоящую из однострочного и многострочного текстовых полей
и двух кнопок "Открыть" и "Сохранить". При клике на первую должен открываться на
чтение файл, чье имя указано в поле класса Entry, а содержимое файла должно
загружаться в поле типа Text.
При клике на вторую кнопку текст, введенный пользователем в экземпляр Text, должен
сохраняться в файле под именем, которое пользователь указал в однострочном текстовом поле.
Файлы будут читаться и записываться в том же каталоге, что и файл скрипта, если
указывать имена файлов без адреса.'''
from tkinter import *

root = Tk()

def open_file():
    file_1 = open(file_name.get())
    file_content.insert(1.0, file_1.read())

def save_file():
    file_2 = open(file_name.get(), 'w')
    file_2.write(file_content.get(1.0, END))

root.title('Save and Open file')

frame = Frame()
frame_file_content = Frame()

file_name = Entry(frame, bd=4, relief=GROOVE, width='25')
button_open = Button(frame, text=' Open file ', command=open_file)
button_save = Button(frame, text=' Save to new one ', command=save_file)

file_content = Text(frame_file_content, bg='#FFFFE0', width='50', height='20', wrap=NONE)
Yscroll = Scrollbar(frame_file_content, command=file_content.yview)
Xscroll = Scrollbar(orient=HORIZONTAL, command=file_content.xview)
file_content.configure(yscrollcommand=Yscroll.set, xscrollcommand=Xscroll.set)

frame.pack()
file_name.pack(side=LEFT)
button_open.pack(side=LEFT)
button_save.pack(side=LEFT)

frame_file_content.pack(fill=BOTH, expand=1)
file_content.pack(side=LEFT, fill=BOTH, expand=1)
Yscroll.pack(side=LEFT, fill=Y)
Xscroll.pack(side=BOTTOM, fill=X)

root.mainloop()
