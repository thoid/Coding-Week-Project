from src.game_data.survival import *
import inquirer


def initialize_game():  # cette fonction va etre utilisée pour effectuer le jeu dans un premier temps sans interface graphique, elle permet d'input les variables
    """Allows players to place their soldiers on the battlefield without a graphic interface, using the terminal.

    Returns:
        tuple: size of the universe
        str: chosen set of rules
        int: maximum number of soldiers allowed per player
    """
    while True:
        height = input("Enter the height of the universe : ")
        try:
            height = int(height)
            assert height > 0
            break
        except ValueError:
            print("Entered value is no number,try again.")
        except AssertionError:
            print("Entered number isn't positive, try again.")

    while True:
        width = (input("Enter the width of the universe (must be an even number) : "))
        try:
            width = int(width)
            assert width % 2 == 0 and width > 0
            break
        except ValueError:
            print("Entered value is no number, try again.")
        except AssertionError:
            print("Entered number isn't positive or even, try again.")

    size = (int(height), int(width))

    mode = inquirer.prompt([inquirer.List(
        "Mode", message="Choose playing mode ", choices=Mode), ])["Mode"]

    while True:
        number_max = (input("Enter the maximum number of cells per player : "))
        try:
            number_max = int(number_max)
            assert number_max > 0
            break
        except ValueError:
            print("Entered value is no number, try again.")
        except AssertionError:
            print("Entered number isn't positive, try again.")
    return size, mode, number_max
