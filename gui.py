from Tkinter import *
from main import *
from RPI import *
import time
# base window
root = Tk()
# window title
root.title('Steam')
# window icon
# root.iconphoto(False,tkinter.PhotoImage(file='Steam.png'))
# resizing is false
root.resizable(width=True, height=False)
# set window size
root.geometry('800x400')


class check_button(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.b = False

    def checkloop(self):
        while True:
            if GPIO.input(23) == 1:
                if self.b == False:
                    hide_show()
                    time.sleep(0.2)
                    self.b = True
                else:

                    self.b = False
                while GPIO.input(23) == 1: pass


def hide_info():
    label_naam.grid_forget()
    label_info.grid_forget()


def hide_show():
    hide_info()
    show_info()


var_naam = StringVar()
var_naam.set(eerste_spel_naam())

var_info = StringVar()
var_info.set(eerste_spel_info())
label_naam = Label(
    master=root,
    textvariable=var_naam,
    background='white',
    font='Helvetica 25 bold'
)
label_info = Message(
    master=root,
    background='white',
    width=180,
    textvariable=var_info
)


def show_info():
    var_naam.set(eerste_spel_naam())
    label_naam.config(textvariable=var_naam)
    var_info.set(eerste_spel_info())
    label_info.config(textvariable=var_info)
    label_naam.grid(
        row=0,
        column=0,
        sticky=''
    )
    label_info.grid(
        row=0,
        column=1,
        sticky=''
    )
    global teller
    teller += 1


next_button = Button(
    master=root,
    text='Next',
    command=hide_show
)
next_button.grid(
    row=2,
    column=0,
    sticky='w'
)
# show window
chk1 = check_button()
c1 = Thread(target=chk1.checkloop)
c1.start()
mainloop()
