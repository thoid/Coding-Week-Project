import sys, os
sys.path.append( os.path.split(os.path.dirname(os.path.abspath(__file__)))[0])

import numpy as np
from src.game_data.survival import *

def test_survival():
    """tests the validity of the function survival
    """
    a=np.array([[0,0,0],[0,0,0],[0,0,0]])
    b=np.array([[0,1,0],[0,0,2],[0,2,0]])
    c=np.array([[0,1,0],[0,0,1],[0,2,0]])
    d=np.array([[2,1,1],[2,1,0],[0,0,0]])
    e=np.array([[0,0,0],[0,1,0],[2,2,2]])

    #test de distancing
    assert(cell_distancing(a,(1,1))==0)
    assert(cell_distancing(b,(1,1))==2)
    assert(cell_distancing(c,(1,1))==1)
    assert(cell_distancing(d,(1,1))==0)
    assert(cell_distancing(e,(1,1))==1)

    #test de contagion
    assert(cell_contagion(a,(1,1))==0)
    assert(cell_contagion(b,(1,1))==2)
    assert(cell_contagion(c,(1,1))==1)
    assert(cell_contagion(d,(1,1))==0)
    assert(cell_contagion(e,(1,1))==2)
    
    #test de cell army
    assert(cell_army(a,(1,1))==0)
    assert(cell_army(b,(1,1))==0)
    assert(cell_army(c,(1,1))==0)
    assert(cell_army(d,(1,1))==2)
    assert(cell_army(e,(1,1))==2)
    
    #test de labyrinth
    assert(cell_labyrinth(a,(1,1))==0)
    assert(cell_labyrinth(b,(1,1))==2)
    assert(cell_labyrinth(c,(1,1))==1)
    assert(cell_labyrinth(d,(1,1))==1)
    assert(cell_labyrinth(e,(1,1))==2)

test_survival()
