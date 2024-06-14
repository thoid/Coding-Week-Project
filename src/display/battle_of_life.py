from tkinter import *

from src.display.display import *
from src.end.end_battle_of_life import end_battle_of_life
from src.end.game_end import game_end
from src.game_data.survival import *


def battle_of_life():
    """THE ACTUAL GAAAAME yeeeeeeeah
    """
    gui = Tk()
    gui.geometry("300x370")

    def getEntry():
        res = myEntry.get()
        res2 = myEntry2.get()
        res3 = myEntry3.get()
        line = listbox1.curselection()[0]
        res4 = listbox1.get(line)
        affich((int(res), int(res2)), int(res3), int(res3), str(res4))



    #Entry
    label = Label(gui, text="Entrer nombre ligne univers:")
    label.pack(pady=10)

    myEntry = Entry(gui, width=40)
    myEntry.pack()

    label2 = Label(gui, text="Entrer nombre colonne univers: ")
    label2.pack(pady=10)

    myEntry2 = Entry(gui, width=40)
    myEntry2.pack()

    label3 = Label(gui, text="Entrer nombre case joueur: ")
    label3.pack(pady=10)

    myEntry3 = Entry(gui, width=40)
    myEntry3.pack()

    label4 = Label(gui, text="Choisir mode de jeu: ")
    label4.pack(pady=10)

    my_frame = Frame(gui)
    s = Scrollbar(my_frame, orient=VERTICAL)

    # Add a Listbox Widget
    listbox1 = Listbox(my_frame, height=5, width=25)

    s.config(command=listbox1.yview)
    s.pack(side=RIGHT, fill=Y)
    my_frame.pack()

    listbox1.pack(side=LEFT, fill=BOTH, expand=1)

    # Add values to the Listbox
    for elem in Mode.keys():
        listbox1.insert(END, elem)
        
    
    #Button play
    btn = Button(gui, height=1, width=10, text="Play", command=getEntry)
    btn.pack(pady=10)
    gui.title("Battle of Life")
    gui.mainloop()
