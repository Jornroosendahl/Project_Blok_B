import tkinter
from tkinter import *
from main import *

#base window
root = Tk()
#window title
root.title('Steam')
#window icon
#root.iconphoto(False,tkinter.PhotoImage(file='Steam.png'))
#resizing is false
root.resizable(width=True,height=False)
#set window size
root.geometry('800x400')

var_naam = StringVar()
var_naam.set(eerste_spel_naam())

var_info = StringVar()
var_info.set(eerste_spel_info())

label_naam = Label  (
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
    label_info.grid (
                    row=0,
                    column=1,
                    sticky=''
                    )
    global teller
    teller +=1
def hide_info():
    label_naam.grid_forget()
    label_info.grid_forget()
def hide_show():
    hide_info()
    show_info()



# back_button = Button(
#                     master=root,
#                     text='Back',
#                     command = hide_info,
#                     )
# back_button.grid    (
#                     row=1,
#                     column=0,
#                     sticky='w'
#                     )
next_button = Button(
                    master=root,
                    text='Next',
                    command = hide_show
                    )
next_button.grid   (
                    row=2,
                    column=0,
                    sticky='w'
                    )

#show window
#mainloop()

# het importeren van de gespecificeerde module
#import matplotlib.pyplot as plt

# x aswaarden


#x = [10,20,30,40,50,60,70,80,130,220,240,280,300,320,340,360,380,400,420,440,500,550,570,620,630,730,1002,1200]

# corresponderende y-aswaarden

#y = [7.19,3.99,3.99,3.99,3.99,3.99,7.19,7.19,3.99,7.19,7.19,0.0,7.19,3.99,0.0,0.0,5.79,7.19,5.79,0.0,7.19,7.19,0.0,7.19,0.0,0.0,5.99,3.99,]

# het plotten van de punten

#plt.plot(x, y)

# het benoemen van de x-as

#plt.xlabel('x – as')

# het benoemen van de y-as

#plt.ylabel('y – as')

# het geven van een titel aan mijn grafiek

#plt.title('Verhouding prijs en appid')

# functie om de plot aan te duiden

#plt.show()

#show window
mainloop()

# het importeren van de gespecificeerde module
import matplotlib.pyplot as plt

# x aswaarden


x = [10,20,30,40,50,60,70,80,130,220,240,280,300,320,340,360,380,400,420,440,500,550,570,620,630,730,1002,1200]

# corresponderende y-aswaarden

y = [317,62,34,184,415,10,83,43,205,402,400,214,134,32,81,184,137,301,623,278,566,801,520,83,6502,0,258,0]

# het plotten van de punten

plt.plot(x, y)

# het benoemen van de x-as

plt.xlabel('x – as')

# het benoemen van de y-as

plt.ylabel('y – as')

# het geven van een titel aan mijn grafiek

plt.title('Verhouding median playtime en appid')

# functie om de plot aan te duiden

plt.show()