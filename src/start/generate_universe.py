import numpy as np


def generate_universe(size):
    """generates an empty universe

    Args:
        size (tuple): (number of lines,number of colums)

    Returns:
        array: array filled with zeros representing and empty universe.
    """
    return np.zeros(size)
