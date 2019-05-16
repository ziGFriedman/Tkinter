'''Напишите программу по описанию. Размеры многострочного текстового поля определяются
значениями, введенными в однострочные текстовые поля. Изменение размера происходит
при нажатии мышью на кнопку, а также при нажатии клавиши Enter.
Цвет фона экземпляра Text светлосерый (lightgrey), когда поле не в фокусе, и белый,
когда имеет фокус.
Событие получения фокуса обозначается как <FocusIn>, потери – как <FocusOut>.
Для справки: фокус перемещается по виджетам при нажатии Tab, Ctrl+Tab, Shift+Tab, а
также при клике по ним мышью (к кнопкам последнее не относится).'''

from tkinter import  *

def bg_fin(event):
    text['bg'] = 'white'

def bg_fout(event):
    text['bg'] = 'lightgray'
    
def tw_change(event):
    a = e1.get()
    b = e2.get()
    if a and b != '':
        try:
            int(a) and int(b)
            text.delete(1.0, END)
            text['width'] = a
            text['height'] = b
        except:
            text.delete(1.0,END)
            text.insert(1.0,'Введите только цифры')
    else:
        text.delete(1.0, END)
        text.insert(0.0 , 'Введите два значение')

root= Tk()

fr1 = Frame(root)
fr2 = Frame(fr1)
fr1.pack(side = TOP)
fr2.pack(side = RIGHT)

e1 =Entry(fr1, width = 5)
e2 = Entry(fr1, width = 5)
b =Button(fr2, text = 'Изменить')
text = Text(bg = 'lightgray')

e1.pack(pady = 2)
e2.pack(pady = 2)
b.pack()
text.pack()

text.bind('<FocusIn>', bg_fin)
text.bind('<FocusOut>', bg_fout)
b.bind('<Button-1>', tw_change)
e1.bind('<Return>', tw_change)
e2.bind('<Return>', tw_change)

root.mainloop()
