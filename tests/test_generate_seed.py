
import sys, os
sys.path.append( os.path.split(os.path.dirname(os.path.abspath(__file__)))[0])

from src.start.generate_seed import create_seed, add_seed_to_universe
from src.start.generate_universe import generate_universe
import numpy as np
from src.game_data.seeds import *


def test_create_seed():
    """tests the validity of create_seed
    """
    seed = create_seed("r_pentomino")
    assert (seed == [[0, 1, 1], [1, 1, 0], [0, 1, 0]]).all()


def test_add_seed_to_universe():
    """tests the validity of add_seed_to_the_universe
    """
    player = 2
    universe = generate_universe((6, 6))
    # Attention, player = 2 donc len(universe[0])//2 < x_start < len(universe)
    universe = add_seed_to_universe("r_pentomino", universe, (3, 3), player)
    # print(universe)
    test_equality = np.array(universe == np.array([[0, 0, 0, 0, 0, 0],
                                                  [0, 0, 0, 0, 0, 0],
                                                   [0, 0, 0, 0, 0, 0],
                                                   [0, 0, 0, 0, 2, 2],
                                                   [0, 0, 0, 2, 2, 0],
                                                   [0, 0, 0, 0, 2, 0]], dtype=np.uint8))
    assert test_equality.all()


test_add_seed_to_universe()