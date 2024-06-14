import sys, os
sys.path.append( os.path.split(os.path.dirname(os.path.abspath(__file__)))[0])

from src.display.iterate_tkinter import *

def test_convert():
    """tests the validity of the fonction "convert"
    """
    gameoflife=Tk()
    uni=Canvas(gameoflife,bg='white',height=1000,width=1000)
    uni.grid()
    convert(np.array([[0,1,2]]),uni,300)
    mainloop()

def test_update_carré():
    """test the validity of the function update_carré
    """
    gameoflife=Tk()
    uni=Canvas(gameoflife,bg='white',height=1000,width=1000)
    uni.grid()
    a=Canvas.create_rectangle(uni,0,1000,0,1000,fill='red')
    update_carré(0,uni,a)
    assert(canvas.itemcget(a, 'fill')=='black')

def test_iterate_tkinter():
    """tests the validity of the function "iterate_tkinter"
    """
   iterate_tkinter(np.array([
        [0, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 1, 0, 1, 2],
        [0, 0, 0, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0],
        [1, 0, 2, 0, 0, 0, 0, 0],
    ]),80,'distancing',0,0)

