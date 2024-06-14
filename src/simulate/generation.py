import numpy as np

from src.game_data.survival import *


def generation(universe: np.array, mode: str, number_red: int, number_blue: int) -> np.array:
    """updates the battlefield according to the chosen rules

    Args:
        universe (np.array): array representing the universe
        mode (str): chosen set of rules
        number_red (int): number of red soldiers alive on the battlefield
        number_blue (int): number of blue soldiers alive on the battlefield

    Returns:
        np.array, int, int: updated universe and numbers of soldiers still alive
    """
    copy_universe = np.array(universe)
    for i in range(len(universe)):
        for j in range(len(universe[0])):
            input = copy_universe[i][j]
            output = Mode[mode](copy_universe, (i, j))
            universe[i][j] = output
            if input == 0:
                if output == 1:
                    number_red += 1
                if output == 2:
                    number_blue += 1
            elif input == 1:
                if output == 0:
                    number_red -= 1
                if output == 2:
                    number_red -= 1
                    number_blue += 1
            elif input == 2:
                if output == 0:
                    number_blue -= 1
                if output == 1:
                    number_red += 1
                    number_blue -= 1

    return universe, number_red, number_blue
