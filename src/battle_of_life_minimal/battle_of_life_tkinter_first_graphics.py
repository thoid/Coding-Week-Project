from src.battle_of_life_minimal.initialize import initialize_game
from src.start.generate_universe import generate_universe
from src.battle_of_life_minimal.place_seeds import place_seeds
from src.display.iterate_tkinter import iterate_tkinter
from src.end.game_end import game_end


def battle_of_life_tkinter():
    """First version of the game with no grafic interface to place blocks.
    """
    size, mode, number_max = initialize_game()
    universe = generate_universe(size)
    print(universe)
    a = max(size)
    b = 790//a
    number_red, number_blue = place_seeds(universe, number_max)
    number_red, number_blue = iterate_tkinter(
        universe, b, mode, number_red, number_blue)
    print("The winner is player ", game_end(number_red, number_blue))


battle_of_life_tkinter()
