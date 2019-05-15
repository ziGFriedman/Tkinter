from tkinter import *
root = Tk()
fr1 = Frame()
fr2 = Frame()
fr3 = Frame()

fruits = ['apple', "bananas", "carrot", "bread", "butter", "meat", "milk", "potato", "pineapple"]
fruits2 = []

def sel():
    if lBox.curselection() != '':
        a = list(lBox.curselection())
        a.reverse()
        for i in a:
            lBox2.insert(END, lBox.get(i))
            lBox.delete(i)

def sel2():
    if lBox2.curselection() != '':
        a = list(lBox2.curselection())
        a.reverse()
        for i in a:
            lBox.insert(END, lBox2.get(i))
            lBox2.delete(i)

lBox = Listbox(fr1, selectmode = EXTENDED)

for i in fruits:
    lBox.insert(END, i)

b1 = Button(fr2, width = 10, text = '>>>', command = sel)
b2 = Button(fr2, width = 10, text = '<<<', command = sel2)

for i in fruits2:
    lBox.insert(END, i)

lBox2 = Listbox(fr3, selectmode = EXTENDED)

lBox.pack()
b1.pack()
b2.pack()
lBox2.pack()

fr1.pack(side = LEFT)
fr2.pack(side = LEFT)
fr3.pack(side = LEFT)

root.mainloop()
