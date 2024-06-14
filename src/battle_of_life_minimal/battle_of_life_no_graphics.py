from src.battle_of_life_minimal.initialize import initialize_game
from src.start.generate_universe import generate_universe
from src.battle_of_life_minimal.place_seeds import place_seeds
from src.battle_of_life_minimal.iterate import iterate
from src.end.game_end import game_end


def battle_of_life(tmp=0.2):
    """The game without the graphic interface. Only displays the winner and each's army's number of fighters still alive.

    Args:
        tmp (float, optional): Time interval the program waits between displaying two successive generations. In seconds. Defaults to 0.2.
    """
    size, mode, number_max = initialize_game()
    universe = generate_universe(size)
    print(universe)
    number_red, number_blue = place_seeds(universe, number_max)
    number_red, number_blue = iterate(
        universe, mode, number_red, number_blue, tmp)
    print("The winner is player ", game_end(number_red, number_blue))
    
battle_of_life()
