from tkinter import *
from main import *
from RPI import *
from PIL import ImageTk, Image
import sys
import tkinter.messagebox as messagebox
# import matplotlib.pyplot as plt

with open('steam.json') as json_file:
    data = json.load(json_file)


# base window
root = Tk()
# window title
root.title('Steam')
# window icon
# root.iconphoto(False,tkinter.PhotoImage(file='Steam.png'))
# resizing is false
root.resizable(width=True, height=False)

#set background image
bg = ImageTk.PhotoImage(Image.open('background.jpg'))
bg_label=Label(master=root,
               image=bg)
bg_label.place(x=0,y=0)

# set window size
root.geometry('800x800')


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


def hide_info():
    label_naam.grid_forget()
    label_info.grid_forget()


def hide_show():
    hide_info()
    show_info()
    hc595(rating())


def entry_waarde():
    waarde = zoekveld.get()
    return waarde


def search():
    global label_zoeknaam
    for i in data[0:50]:
        for x in i:
            if x == 'name':
                if entry_waarde() in i[x] or entry_waarde() in str(i[x]).lower():
                    try:
                        label_zoeknaam.destroy()
                        # label_zoekinfo.destroy()
                    except:
                        print('Nothing to destroy')
                    label_zoeknaam = Label(master=root,
                                           text=i[x],
                                           background='white',
                                           font='Helvetica 25 bold')
                    zoek_naam = i[x]

                    label_zoeknaam.grid(row=7,
                                        column=0,
                                        sticky='w')
                    for x in i:
                        if x == 'appid':
                            zoek_id = 'AppID:' + str(i[x])
                        if x == 'release_date':
                            zoek_release_date = 'Release_date:' + str(i[x])
                        if x == 'developer':
                            zoek_developer = 'Developer:' + str(i[x])
                        if x == 'publisher':
                            zoek_publisher = 'Publisher:' + str(i[x])
                        if x == 'platforms':
                            zoek_platforms = 'Platforms:' + str(i[x])
                        if x == 'genres':
                            zoek_genres = 'Genres:' + str(i[x])
                        if x == 'price':
                            zoek_price = 'Price:' + str(i[x])
                    zoek_info = zoek_id + '\n' + zoek_release_date + '\n' + zoek_developer + '\n' + zoek_publisher + '\n' + zoek_platforms + '\n' + zoek_genres + '\n' + zoek_price

                    label_zoekinfo = Label(master=root,
                                           text=zoek_info,
                                           background='white')
                    # label_zoekinfo.grid(row=8,
                    #                     column=0,
                    #                     sticky='w')
                    messagebox.showinfo(zoek_naam, zoek_info)


def forget():
    global label_zoeknaam
    label_zoeknaam.destroy()


def Entry_waarde():
    waarde = sorteerveld.get()
    return waarde

def my_sort():
    global label_zoeknaam
    newlst = data[0:50]
    Jewan = Entry_waarde()
    text = ('')
    while True:
        #Controle variabele aanmaken.
        check = 0
        #Voor elke getal van 0 tot getal voor input, dan gaat het door de conditie.
        for i in range(0, len(newlst) - 1):
            #Als de index van newlst[i] groter is dan newlst[i+1]
            if newlst[i][Jewan] > newlst[i + 1][Jewan]:
                #Verander ze dan van plek/positie
                newlst[i], newlst[i + 1] = newlst[i + 1], newlst[i]
                check += 1
        #Als de check gelijk is aan 0, return newlst
        if check == 0:
            for b in newlst:
                text = text + str(b['name']) + '\n'
                if Jewan != 'name':
                    text = text + str(b[Jewan]) + '\n'
            break
    messagebox.showinfo('gesorteerd', text)
def Entrywaarde():
    waarde = frequentieveld.get()
    return waarde

def freq():
    global label_zoeknaam
    newlst = data[0:50]
    Jewan = Entrywaarde()
    freq = {}
    for i in newlst:
        if (i[Jewan] in freq):  # hierin wordt er gekeken of er een i in freq voorkomt.
            freq[i[Jewan]] += 1
        if i[Jewan] not in freq:  # Als de i niet in de freq voorkomt.
            freq[i[Jewan]] = 1
    messagebox.showinfo('frequentie', freq)
     # Hiermee wordt de waarde frequenties gereturnd.

def rnge():
    global label_zoeknaam
    newlst = data
    temp = 0
    for i in newlst:
        if i['price'] > temp:
            temp = i['price']
    temp2 = sys.maxsize
    for i in newlst:
        if i['price'] < temp2:
            temp2 = i['price']
    messagebox.showinfo('range:',temp - temp2)




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

zoekveld = Entry    (
                    master=root,

                    )
zoekveld.grid       (
                    row=4,
                    column=0,
                    sticky='w'
                    )
zoekknop = Button   (master=root,
                     text='search',
                     command=search)
zoekknop.grid       (row=5,
                     column=0,
                     sticky='w')

sorteerveld = Entry(
                    master=root,

                   )
sorteerveld.grid   (
                    row=35,
                    column=0,
                    sticky='w'
                    )
sorteerknop = Button(master=root,
                     text='sort',
                     command=my_sort)
sorteerknop.grid    (row=40,
                     column=0,
                     sticky='w'
                    )
frequentieveld = Entry(
                      master=root,
                      )
frequentieveld.grid (
                     row=10,
                     column=0,
                     sticky='w'
)
# rngeveld = Entry(
#                  master=root
#                  )
# rngeveld.grid (
#                row=14,
#                column=0,
#                sticky='w'
#               )
rngeknop = Button(master=root,
                  text='range',
                  command=rnge)
rngeknop.grid   (
                row=15,
                column=0,
                sticky='w'
                )
frequentieknop = Button(master=root,
                        text='frequentie',
                        command=freq
                        )
frequentieknop.grid     (
                        row=12,
                        column=0,
                        sticky='w'
                        )
label_rngeveld = Label(
                   master=root,
                   text='range:')

label_rngeveld.grid(
                    row=13,
                    column=0,
                    sticky='w')

label_zoekveld = Label(
                    master=root,
                    text='Zoekveld:')
label_zoekveld.grid (row=3,
                     column=0,
                     sticky='w')

label_sorteerveld = Label(
                    master=root,
                    text='Sorteerveld:')
label_sorteerveld.grid (row=30,
                        column=0,
                        sticky='w')
label_frequentieveld = Label(
                            master=root,
                            text='Frequentieveld:',)
label_frequentieveld.grid (row=9,
                           column=0,
                           sticky='w')

# het importeren van de gespecificeerde module
# import matplotlib.pyplot as plt

# x aswaarden


# x = [10,20,30,40,50,60,70,80,130,220,240,280,300,320,340,360,380,400,420,440,500,550,570,620,630,730,1002,1200]

# corresponderende y-aswaarden

# y = [7.19,3.99,3.99,3.99,3.99,3.99,7.19,7.19,3.99,7.19,7.19,0.0,7.19,3.99,0.0,0.0,5.79,7.19,5.79,0.0,7.19,7.19,0.0,7.19,0.0,0.0,5.99,3.99,]

# het plotten van de punten

# plt.plot(x, y)

# het benoemen van de x-as

# plt.xlabel('x – as')

# het benoemen van de y-as

# plt.ylabel('y – as')

# het geven van een titel aan mijn grafiek

# plt.title('Verhouding prijs en appid')

# functie om de plot aan te duiden

# plt.show()

#show window
chk1 = check_button()
c1 = Thread(target=chk1.checkloop)
c1.start()
mainloop()

# het importeren van de gespecificeerde module


# x aswaarden


x = [10, 20, 30, 40, 50, 60, 70, 80, 130, 220, 240, 280, 300, 320, 340, 360, 380, 400, 420, 440, 500, 550, 570, 620,
     630, 730, 1002, 1200]

# corresponderende y-aswaarden

y = [317, 62, 34, 184, 415, 10, 83, 43, 205, 402, 400, 214, 134, 32, 81, 184, 137, 301, 623, 278, 566, 801, 520, 83,
     6502, 0, 258, 0]

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
