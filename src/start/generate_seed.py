import numpy as np
from src.game_data.seeds import *


def create_seed(seed_type):
    """Creates a seed corresponding to a given name 

    Args:
        seed_type (str): name of the seed

    Returns:
        list: seed as an array
    """
    return np.array(type_seed[seed_type])


def add_seed_to_universe(seed, universe, position, player):
    """modifies an universe by adding a given seed in a given position. The nature of a seed (array filled with ones or twos) depends on the player's number)

    Args:
        seed (str): name of the seed
        universe (array): starting universe before adding the seed
        position (tuple): (starting colum, starting line). Coordonates of the top left corner of the seed.
        player (int): which player is playing

    Raises:
        Exception: Player 1 must place their seed is the left half of the universe and player 2 in the right half of the universe"
        Exception: the length of the seed should not exceed that of the universe
        Exception: the width of the seed should not exceed that of the universe

    Returns:
        array: modified universe with added seed 
    """
    x_start = position[0]
    y_start = position[1]
    hauteur = len(seed)
    largeur = len(seed[0])
    hautU = len(universe)
    largU = len(universe[0])//2
    # Si le deuxième joueur execute le programme, les coordonnées doivent être dans la moitié droite du tableau. On se ramène ensuite à travailler dans un demi tableau et on se décalera d'un demi tableau après si c'est le player 2.
    x_start = (x_start-(player-1)*largU) % len(universe[0])
    y_start = hautU - y_start
    y_end = y_start - hauteur
    x_end = x_start + largeur
    if x_start > largU:
        raise Exception(
            "Player 1 must place their seed is the left half of the universe and player 2 in the right half of the universe")
    if hauteur > hautU:
        raise Exception('the seed should not be taller than the universe')
    if largeur > largU:
        raise Exception('the seed should not be taller than the universe')
    for i in range(y_end, y_start):
        for j in range(x_start, x_end):
            # Si le player 2 joue, on se décale d'un demi tableau.
            universe[i % hautU][j % largU+largU * (player - 1)] = player * \
                seed[i-y_start][j-x_start]
    return universe
