from tkinter import *
from main import *

#base window
root = Tk()
#window title
root.title('Steam')
#resizing is false
root.resizable(width=False,height=False)
#set window size
root.geometry('500x400')

var = StringVar()
var.set(eerste_spel_naam())


label_naam = Label(master=root,
                   textvariable=var,
                   background='white')
label_naam.pack()

left_button = Button(master=root,
                     text='Left',
                     command = '')
left_button.pack()

right_button = Button(master=root,
                     text='Right',
                     command = '')
right_button.pack()

#show window
mainloop()