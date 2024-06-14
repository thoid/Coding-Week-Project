from tkinter import *


from src.start.generate_seed import *
from src.start.generate_universe import *
from src.display.iterate_tkinter import *
from src.end.end_battle_of_life import end_battle_of_life
from src.end.game_end import game_end
from src.game_data.seeds import *

# Paramètres à définir avant

color1 = "red"
color2 = "blue"
default_color = "white"
player = 1


def affich(size, compt_red, compt_blue, mode):
    """Displays the evolution of the universe throughout the game

    Args:
        size (tuple): Size of the universe
        compt_red (int): Nomber of red soldiers alive at the beginning in the universe
        compt_blue (int): Number of blue soldiers alive at the beginning in the universe
        mode (str): set of rules used to decide when blocks spawn or die

    Returns:
        animation: the evolution of the universe
    """


    window = Tk()
    global player

    # Ajout de seed
    def add_seed_button(seed, player, last_clicked):
        """Allow players to place their soldiers on the battlefield by clicking on a chosen square

        Args:
            seed (str): the type of seed they want to add
            player (int): which player is playing
            last_clicked(tuple): last button clicked
        """

        global color1
        global color2
        global default_color
        if int(compteur_red["text"])-taille_seed(seed) < 0 and player == 1:
            print("pas assez de case pour le joueur 1")
        elif int(compteur_blue["text"])-taille_seed(seed) < 0 and player == 2:
            print("pas assez de case pour le joueur 2")
        elif seed == "blank":
            dic[last_clicked]["bg"] = default_color
        else:
            (row, column) = last_clicked
            x = column
            y = size[0] - row - 1
            univ = add_seed_to_universe(
                create_seed(seed), generate_universe(size), (x, y), player)
            for i in range(len(univ)):
                for j in range(len(univ[0])):
                    if univ[i][j] == 1:
                        dic[i, j]["bg"] = color1
                    elif univ[i][j] == 2:
                        dic[i, j]["bg"] = color2
        matrice_color(size, compt_red, compt_blue)

    # Changer de joueur
    def change_player():
        """Allow players to take turns by clicking on a button
        """

        global player
        if player == 1:
            player = 2
        else:
            player = 1
        current_player["text"] = "Current Player: %s" % player

    # Modifie le compteur et renvoie la matrice de l'affichage en tableau numpy
    def matrice_color(size, c_red, c_blue):
        """Updates the red block and blue block numbers and returns a matrix containing the color of each square and a number among 0, 1 and 2.

        Args:
            size (tuple): size of the universe
            c_red (int): number of red soldiers alive at the beginning on the battlefield
            c_blue (_type_): number of red soldiers alive at the beginning on the battlefield

        Returns:
            a matrix the same size as the universe contening the information of the color of each square.
        """

        global color1
        global color2
        global default_color
        b = 0
        r = 0
        unive = np.zeros(size)
        for i in range(size[0]):
            for j in range(size[1]):
                if dic[i, j]["bg"] == color1:
                    unive[i][j] = 1
                    r += 1

                elif dic[i, j]["bg"] == color2:
                    unive[i][j] = 2
                    b += 1

        compteur_red["text"] = str(c_red-r)
        compteur_blue["text"] = str(c_blue-b)
        return unive

    # Renvoie la taille de carré rempli d'une seed
    def taille_seed(seed_type):
        """Calculates the number of blocks of a seed

        Args:
            seed_type (str): the type of seed which size we want to calculate

        Returns:
            int: Number of blocks of the seed
        """

        seed = create_seed(seed_type)
        S = 0
        for i in range(len(seed)):
            for j in range(len(seed[0])):
                if seed[i][j] == 1:
                    S += 1
        return S

    # reinitialiser
    def reinitialise():
        """reinitialises the game : every square is colored back to white.
        """

        for i in range(size[0]):
            for j in range(size[1]):
                dic[i, j]["bg"] = default_color
        matrice_color(size, compt_red, compt_blue)

    # jouer
    def Playy():
        """shows the evolution of the numbres of soldiers and triggers the end animation.
        """
        a = max(size)
        b = 790//a
        number_red, number_blue, t = iterate_tkinter(matrice_color(
            size, compt_red, compt_blue), b, mode, compt_red-int(compteur_red["text"]), compt_blue-int(compteur_blue["text"]))

   
    #compteur bleu et rouge
    compteur_red = Label(window, text="%s" % compt_red,
                         font='Arial 15 bold', fg='red')
    compteur_red.grid(column=size[1], row=10, rowspan=2)

    compteur_blue = Label(window, text="%s" % compt_blue,
                          font='Arial 15 bold', fg='blue')
    compteur_blue.grid(column=size[1], row=12, rowspan=2)

    current_player = Label(window, text="Current Player: %s" % player)
    current_player.grid(column=size[1], row=8)

    my_frame = Frame(window)
    s = Scrollbar(my_frame, orient=VERTICAL)

    # Add a Listbox Widget
    listbox = Listbox(my_frame, height=8, width=20)

    s.config(command=listbox.yview)
    s.pack(side=RIGHT, fill=Y)

    listbox.pack(side=LEFT, fill=BOTH, expand=1)

    my_frame.grid(column=size[1], row=0, rowspan=10, columnspan=2, sticky=N)

    # Add values to the Listbox
    for cle in type_seed.keys():
        listbox.insert(END, cle)

    listbox.selection_set(0)
    pixelVirtual = PhotoImage(master=window, width=1, height=1)
    
    
    # Création grille de bouton
    dic = {}
    for x in range(size[0]):
        for y in range(size[1]):
            b = Button(window, bg=default_color,
                       activebackground=default_color, image=pixelVirtual, width=20, height=20, compound="c")
            b.grid(column=y, row=x)
            dic[x, y] = b
            dic[x, y]["command"] = lambda x=x, y=y: add_seed_button(
                listbox.get(listbox.curselection()), player, (x, y))

    
    #Button play, reset, change player
    b_player = Button(window, text="Change Player:", command=change_player)
    b_player.grid(column=size[1], row=6)

    b_play = Button(window, text="Play", command=Playy)
    b_play.grid(column=size[1], row=14)

    b_rei = Button(window, text="Reset", command=reinitialise)
    b_rei.grid(column=size[1], row=16)



    window.title("Battle of Life")
    window.mainloop()
