import time

from src.simulate.generation import generation
from src.simulate.game_finished import game_finished
from src.end.game_end import game_end


def iterate(universe, mode, number_red, number_blue, tmp=10):
    """triggers the succession of generations

    Args:
        universe (array): array representing the universe
        mode (str): chosen set of rules
        number_red (int): number of red soldiers alive
        number_blue (int): number of blue soldiers alive
        tmp (int, optional): number of milliseconds between two generations. Defaults to 10.

    Returns:
       int : the updated numbers of red and blue soldiers alive
    """
    timer = 0
    print(universe)
    while not game_finished(number_red, number_blue, timer):
        universe, number_red, number_blue = generation(
            universe, mode, number_red, number_blue)
        print("\n")
        print(universe)
        print("Number_red = ", number_red)
        print("Number_blue = ", number_blue)
        print("\n")
        time.sleep(tmp)
        timer += 1
    return number_red, number_blue
