import numpy as np

from src.generate_universe import generate_universe
from pytest import *


def test_generate_universe():
    assert (generate_universe((4, 4)) == np.array(
        [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])).all()
    print ("No error was found!")
    
test_generate_universe()
