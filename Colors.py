'''Напишите программу, состоящую из семи кнопок, цвета которых соответствуют
цветам радуги. При нажатии на ту или иную кнопку в текстовое поле должен
вставляться код цвета, а в метку – название цвета.
Коды цветов в шестнадцатеричной кодировке: #ff0000 – красный, #ff7d00 – оранжевый,
#ffff00 – желтый, #00ff00 – зеленый, #007dff – голубой, #0000ff – синий,
#7d00ff – фиолетовый.
Для выравнивания строки по центру в текстовом поле используется
свойство justify со значением CENTER.'''

from tkinter import *

class Color:

    color = {
        '#ff0000' : 'красный',
        '#ff7d00' : 'оранжевый',
        '#ffff00' : 'желтый',
        '#00ff00' : 'зеленый',
        '#007dff' : 'голубой',
        '#0000ff' : 'синий',
        '#7d00ff' : 'фиолетовый',
    }

    def __init__(self, master):
        self.label = Label(master, text='нажми на кнопку', anchor='c')
        self.label.pack()
        self.entry = Entry(master, justify=CENTER)
        self.entry.pack()
        for key, value in self.color.items():
            exec('Button(master, width = 18, command = self.key{2}value, bg = "{0}", text = "{1}").pack()'.
                format(key, value, key[1:]))    # exec - динамически генерируемый код

    for key, value in color.items():
        def bindedfunc(self, v = value, k = key):
            self.label["text"] = v
            self.entry.delete(0, END)
            self.entry.insert(0, "{}".format(k))

        exec('key{}value = bindedfunc'.format(key[1:]))

root = Tk()
root.geometry("200x245")
root.title("Радуга цвета")
app = Color(root)

root.mainloop()
