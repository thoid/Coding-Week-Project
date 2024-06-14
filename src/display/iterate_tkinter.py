from tkinter import *
from functools import partial
import numpy as np

from src.simulate.generation import generation
from src.simulate.game_finished import game_finished
from src.end.game_end import *
from src.end.end_battle_of_life import *


def convert(universe: np.array, uni: Canvas, unit: int):
    """Converts the array representing the univers into a canvas

    Args:
        universe (np.array): the representation of the universe as an array
        uni (Canvas): the representation of the universe as an array
        unit (int): the size of each square

    Returns:
        list: list of blue, red and black canvas rectangle representing the state of the univers 
    """
    (m, n) = np.shape(universe)
    # on va renvoyer une liste d'indices des carrés tracés qui nous servira plus tard pour les modifier
    # au passage cette fonction trace des carrés sur un widget canvas pour un univers donné
    c = []
    for i in range(m):
        c += [[]]
        for j in range(n):
            if universe[i][j] == 1:
                # carré rouge si la valeur est 1
                c[i] += [Canvas.create_rectangle(uni, unit*j,
                                                 unit*i, unit*(j+1), unit*(i+1), fill='red')]
            elif universe[i][j] == 2:
                # carré bleu si la valeur est 2
                c[i] += [Canvas.create_rectangle(uni, unit*j,
                                                 unit*i, unit*(j+1), unit*(i+1), fill='blue')]
            else:
                # carré noir si la cellule est morte
                c[i] += [Canvas.create_rectangle(uni, unit*j,
                                                 unit*i, unit*(j+1), unit*(i+1), fill='black')]
    return c


def update_carré(cell_value: int, canvas: Canvas, item_id: int):
    """updates the color of a square when the value in the corresponding position of the matrix changes
    """
    # cette fonction a pour but de changer la couleur d'un carré une foi que la valeur a été cahngée dans la matrice
    # on utilise le module canvas
    fill = canvas.itemcget(item_id, 'fill')
    # on regarde la valeur dans la matrice et on change en conséquence
    if cell_value == 1:
        canvas.itemconfig(item_id, fill='red')
    elif cell_value == 2:
        canvas.itemconfig(item_id, fill='blue')
    elif cell_value == 0:
        canvas.itemconfig(item_id, fill='black')


def show_generation(universe: np.array, uni: Canvas, c: list, mode: str, number_red: int, number_blue: int):
    """Updates the color of every square from one generation to another

    Args:
        universe (np.array): array representing the universe
        uni (Canvas): canvas representing the universe
        c (list): list of every canvas colored rectangle
        mode (str): chosen set of rules
        number_red (int): number of red soldiers still alive on the battlefield
        number_blue (int): number of blue soldiers still alive on the battlefield

    Returns:
        int : number of red and blue players still alive
    """
    # cette fonction met à jour l'ensemble des couleurs des carrés pour une génération d'univers
    universe_bis = np.array(universe)
    # on effectue une génération d'univers
    universe, number_red, number_blue = generation(
        universe, mode, number_red, number_blue)
    (m, n) = np.shape(universe)
    for i in range(m):
        for j in range(n):
            if universe[i][j] != universe_bis[i][j]:
                # on va mettre à jour la couleur de chaque carré concerné par un changement de couleur
                update_carré(universe[i][j], uni, c[i][j])
    return number_red, number_blue


def iterate_tkinter(universe: np.array, unit: int, mode: str, number_red: int, number_blue: int):
    """Shows the evolution of the game on a graphic interface

    Args:
        universe (np.array): matrix representing the universe
        unit (int): size of each square
        mode (str): chosen set of rules
        number_red (int): number of red soldiers still alive
        number_blue (int): number of blue soldiers still alive

    Returns:
        _type_: _description_
    """
    # voilà la fonction qui va nous montrer l'animation, elle va prendre les parametres de la partie, effectuer le jeu tout en montrant l'avancement
    gameoflife = Tk()
    t = 0
    # on definit notre canvas et notre fenetre de jeu
    uni = Canvas(gameoflife, bg='white', height=790, width=790)
    uni.grid()
    # on commence par dessiner tous les carrés à partir de l'univers de départ
    c = convert(universe, uni, unit)

    # l'animation consiste à iterer la fonction show_generation et voir le déroulement du jeu
    def itergame(number_red, number_blue, t):
        """triggers the iteration of the process of evolution from one generation to another

        Args:
            number_red (int): number of red players alive
            number_blue (int): number of blue players alive
            t (int): number of generations which have already gone by
        """
        t += 1
        if not game_finished(number_red, number_blue, t):
            number_red, number_blue = show_generation(
                universe, uni, c, mode, number_red, number_blue)
            gameoflife.after(100, itergame, number_red, number_blue, t)
            compteur = Label(gameoflife, text="{0}".format(number_blue),
                          font='Arial 15 bold', fg='blue',height=1,width=5)
            compteur.grid(column=1,row=0,sticky=NW,rowspan=1,columnspan=1)
            compteur2 = Label(gameoflife, text="{0} ".format(number_red),
                          font='Arial 15 bold', fg='red',height=1,width=5)
            compteur2.grid(column=2,row=0,sticky=NW,rowspan=1,columnspan=1)
        else:
            end_battle_of_life(
                game_end(number_red, number_blue), number_red, number_blue, t)

    gameoflife.after(100, itergame, number_red, number_blue, t)
    gameoflife.mainloop()

    return number_red, number_blue, t
