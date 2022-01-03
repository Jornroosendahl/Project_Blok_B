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

var_naam = StringVar()
var_naam.set(eerste_spel_naam())

var_info = StringVar()
var_info.set(eerste_spel_info())

label_naam = Label(master=root,
                   textvariable=var_naam,
                   background='white')
label_naam.pack()

label_info = Message(master=root,
                   textvariable=var_info,
                   background='white')
label_info.pack()


left_button = Button(master=root,
                     text='Left',
                     command = '',
                     )
left_button.pack(side=LEFT)

right_button = Button(master=root,
                     text='Right',
                     command = '')
right_button.pack(side=RIGHT)

#show window
mainloop()