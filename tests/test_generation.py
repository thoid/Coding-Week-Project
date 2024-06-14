from src.generation import generation
import numpy as np

def test_generation():
    universe = np.zeros((6,6))
    universe[0][2]=1
    universe[0][3]=1
    universe[2][4]=2
    universe[1][4]=2
    result = generation(universe, 'contagion', 2, 2)
    test_equality = np.array(result[0] == np.array([[0., 0., 0., 1., 0., 0.],
       [0., 0., 0., 0., 2., 0.],
       [0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0.]], dtype=np.uint8))
    assert test_equality.all()
    assert result[1]==1
    assert result[2]==1
    print("No error found!")
    
test_generation()
