from random import randint, random
import numpy as np


def cell_distancing(universe: np.array, pos: tuple):
    """unlike the classic game of life, the cell can be in 3 states: dead, red, blue
     we then implement the survival and color change rules for the distancing mode 
    Args:
        universe (np.array): universe we want to update according to this rule 
        pos (tuple): position of the square which color we want to update

    Returns:
        int: the color of the square as a number among 0, 1 and 2.
    """
    nb_voisins = 0
    valeur = 0
    m = pos[0]
    n = pos[1]
    voisins_rouge = 0
    voisins_bleu = 0
    hauteur = len(universe)
    longueur = len(universe[0])
    for i in range(m-1, m+2):  # comptage des voisins vivants et du type de voisin
        for j in range(n-1, n+2):
            if i != m or j != n:
                val_cell = universe[i % hauteur][j % longueur]
                if val_cell == 1:
                    nb_voisins += 1
                    voisins_rouge += 1
                if val_cell == 2:
                    nb_voisins += 1
                    voisins_bleu += 1
    if universe[m][n] == 0 and nb_voisins == 3:  # reproduction
        if voisins_rouge > voisins_bleu:
            valeur = 1
        else:
            valeur = 2
    # sous/surpopulation
    if universe[m][n] != 0 and (nb_voisins == 2 or nb_voisins == 3):
        valeur = universe[m][n]
    return valeur


def cell_contagion(universe: np.array, pos: tuple):
    """unlike the classic game of life, the cell can be in 3 states: dead, red, blue
     we then implement the rules of survival and color change for the contagion mode 

    Args:
        universe (np.array): universe we want to update according to this rule 
        pos (tuple): position of the square which color we want to update

    Returns:
        int: the color of the square as a number among 0, 1 and 2.
    """
    nb_voisins = 0
    valeur = 0
    m = pos[0]
    n = pos[1]
    voisins_rouge = 0
    voisins_bleu = 0
    hauteur = len(universe)
    longueur = len(universe[0])
    for i in range(m-1, m+2):  # comptage des voisins vivants et du type de voisin
        for j in range(n-1, n+2):
            if i != m or j != n:
                val_cell = universe[i % hauteur][j % longueur]
                if val_cell == 1:
                    nb_voisins += 1
                    voisins_rouge += 1
                if val_cell == 2:
                    nb_voisins += 1
                    voisins_bleu += 1
    if universe[m][n] == 0 and nb_voisins == 3:  # reproduction
        if voisins_rouge > voisins_bleu:
            valeur = 1
        else:
            valeur = 2
    # sous/surpopulation/contagion
    if universe[m][n] != 0 and (nb_voisins == 2 or nb_voisins == 3):
        if voisins_rouge > voisins_bleu:
            valeur = 1
        if voisins_bleu > voisins_rouge:
            valeur = 2
        else:
            valeur = universe[m][n]
    return valeur


def cell_army(universe: np.array, pos: tuple):
    """If a cell is surrounded by two or more cells of the opposite color : it dies. Else, it needs two or three neighbours of its own color to survive and three to spawn.

    Args:
        universe (np.array): universe we want to update according to this rule 
        pos (tuple): position of the square which color we want to update

    Returns:
        int: the color of the square as a number among 0, 1 and 2.
    """
    nb_voisins = 0
    valeur = 0
    m = pos[0]
    n = pos[1]
    voisins_rouge = 0
    voisins_bleu = 0
    hauteur = len(universe)
    longueur = len(universe[0])
    for i in range(m-1, m+2):  # comptage des voisins vivants et du type de voisin
        for j in range(n-1, n+2):
            if i != m or j != n:
                val_cell = universe[i % hauteur][j % longueur]
                if val_cell == 1:
                    nb_voisins += 1
                    voisins_rouge += 1
                if val_cell == 2:
                    nb_voisins += 1
                    voisins_bleu += 1
    if universe[m][n] == 0:  # reproduction
        if voisins_rouge == voisins_bleu and nb_voisins != 0:
            a = randint(0, 2)
            valeur = a
        elif (voisins_rouge == 3 or voisins_rouge == 4) and voisins_rouge > voisins_bleu:
            valeur = 1
        elif (voisins_bleu == 3 or voisins_bleu == 4) and voisins_rouge < voisins_bleu:
            valeur = 2
    # mort
    elif universe[m][n] == 1 and voisins_bleu >= 2:
        a = randint(0, 1)
        if a == 0:
            valeur = 0
        else:
            valeur = 2
    elif universe[m][n] == 2 and voisins_rouge >= 2:
        valeur = randint(0, 1)
    elif nb_voisins > 6:
        valeur = 0
    else:
        valeur = universe[m][n]
    return valeur


def cell_labyrinth(universe: np.array, pos: tuple):
    """It's the same rule as the contagion mode except cells also survive when they are surrounded by 4 cells. 

    Args:
        universe (np.array): universe we want to update according to this rule 
        pos (tuple): position of the square which color we want to update

    Returns:
        int: the color of the square as a number among 0, 1 and 2.
    """
    nb_voisins = 0
    valeur = 0
    m = pos[0]
    n = pos[1]
    voisins_rouge = 0
    voisins_bleu = 0
    hauteur = len(universe)
    longueur = len(universe[0])
    for i in range(m-1, m+2):  # comptage des voisins vivants et du type de voisin
        for j in range(n-1, n+2):
            if i != m or j != n:
                val_cell = universe[i % hauteur][j % longueur]
                if val_cell == 1:
                    nb_voisins += 1
                    voisins_rouge += 1
                if val_cell == 2:
                    nb_voisins += 1
                    voisins_bleu += 1
    if universe[m][n] == 0 and nb_voisins == 3:  # reproduction
        if voisins_rouge > voisins_bleu:
            valeur = 1
        else:
            valeur = 2
    # sous/surpopulation/contagion
    if universe[m][n] != 0 and (nb_voisins == 2 or nb_voisins == 3 or nb_voisins == 4):
        if voisins_rouge > voisins_bleu:
            valeur = 1
        if voisins_bleu > voisins_rouge:
            valeur = 2
        else:
            valeur = universe[m][n]
    return valeur


Mode = {"distancing": cell_distancing, "contagion": cell_contagion,
        "army": cell_army, "labyrinth": cell_labyrinth}

a = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
b = np.array([[0, 1, 0], [0, 0, 2], [0, 2, 0]])
c = np.array([[0, 1, 0], [0, 0, 1], [0, 2, 0]])
d = np.array([[2, 1, 1], [2, 1, 0], [0, 0, 0]])
e = np.array([[0, 0, 0], [0, 1, 0], [2, 2, 2]])
