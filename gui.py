import tkinter
from tkinter import *
from main import *

#base window
root = Tk()
#window title
root.title('Steam')
#window icon
root.iconphoto(False,tkinter.PhotoImage(file='Steam.png'))
#resizing is false
root.resizable(width=False,height=False)
#set window size
root.geometry('500x400')

var_naam = StringVar()
var_naam.set(eerste_spel_naam())

var_info = StringVar()
var_info.set(eerste_spel_info())

def info():
    label_naam = Label  (
                    master=root,
                    textvariable=var_naam,
                    background='white',
                    font='Helvetica 25 bold'
                    )
    label_naam.grid(
                    row=0,
                    column=0,
                    sticky=''
                    )
    label_info = Message(
                    master=root,
                    background='white',
                    width=180,
                    textvariable=var_info
                    )
    label_info.grid     (
                    row=0,
                    column=1,
                    sticky=''
                    )

def volgende():
    info()
    global teller
    teller +=1
left_button = Button(
                    master=root,
                    text='Back',
                    command = '',
                    )
left_button.grid    (
                    row=1,
                    column=0,
                    sticky='nes'
                    )
right_button = Button(
                    master=root,
                    text='Next',
                    command = info
                    )
right_button.grid   (
                    row=1,
                    column=1,
                    sticky='w'
                    )

#show window
mainloop()