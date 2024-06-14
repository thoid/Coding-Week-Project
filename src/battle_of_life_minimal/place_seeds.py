import numpy as np
import inquirer

from src.game_data.seeds import *
from src.start.generate_seed import create_seed, add_seed_to_universe


def count_seed(seed):  # Comptage du nombre de cellules vivantes dans un seed donné
    """Counts the number of living cells in a given seed

    Args:
        seed (str): seed under study

    Returns:
        int: number of cells to form it
    """
    count = 0
    height = len(seed)
    width = len(seed[0])
    for i in range(height):
        for j in range(width):
            if seed[i][j] == 1:
                count += 1
    return count


def place_seeds(universe: np.array, number_max: int) -> np.array:
    """Allows players to place their seeds on the battlefield

    Args:
        universe (np.array): array representing the universe
        number_max (int): max number of soldiers allowed per player

    Returns:
        np.array: universe containing the starting seeds
    """
    number_red, number_blue = 0, 0
    while True:
        while True:
            seed = inquirer.prompt([inquirer.List(
                "Seed", message="Player 1, choose a seed ", choices=type_seed), ])["Seed"]
            number_blocks = count_seed(create_seed(seed))
            seed = create_seed(seed)
            try:
                assert len(seed) <= len(universe) and len(
                    seed[0]) <= len(universe[0])//2
                break
            except AssertionError:
                print("The seed should not be taller than the universe")
        try:
            assert number_red + number_blocks <= number_max
        except AssertionError:
            print("Player 1, you've reached maximum block number.")
            break
        number_red += number_blocks

        while True:
            x = input("Player 1, enter the x position of the seed : ")
            try:
                x = int(x)
                assert 0 <= x and x < len(universe[0])//2
                break
            except ValueError:
                print("Entered value is no number,try again.")
            except AssertionError:
                print("Entered number isn't positive, try again.")

        while True:
            y = input("Player 1, enter the y position of the seed : ")
            try:
                y = int(y)
                assert y >= 0
                break
            except ValueError:
                print("Entered value is no number,try again.")
            except AssertionError:
                print("Entered number isn't positive, try again.")

        add_seed_to_universe(seed, universe, (int(x), int(y)), 1)
        print(universe)
        print("Number_red = ", number_red)
        print("Number_blue = ", number_blue)
        check = inquirer.prompt({inquirer.Confirm(
            'confirmed', message="Do you want to continue placing seeds ?", default=True), })["confirmed"]
        if check == False:
            break

    while True:
        while True:
            seed = inquirer.prompt([inquirer.List(
                "Seed", message="Player 2, choose a seed ", choices=type_seed), ])["Seed"]
            number_blocks = count_seed(create_seed(seed))
            seed = create_seed(seed)
            try:
                assert len(seed) <= len(universe) and len(
                    seed[0]) <= len(universe[0])//2
                break
            except AssertionError:
                print("The seed should not be taller than the universe")
        try:
            assert number_blue + number_blocks <= number_max
        except AssertionError:
            print("Player 2, you've reached maximum block number.")
            break
        number_blue += number_blocks

        while True:
            x = input("Player 2, enter the x position of the seed : ")
            try:
                x = int(x)
                assert len(universe[0])//2 <= x and x <= len(universe[0])
                break
            except ValueError:
                print("Entered value is no number,try again.")
            except AssertionError:
                print("Player 1 must place their seed in the left half of the universe.")

        while True:
            y = input("Player 2, enter the y position of the seed : ")
            try:
                y = int(y)
                assert y >= 0
                break
            except ValueError:
                print("Entered value is no number,try again.")
            except AssertionError:
                print(
                    "Player 2 must place their seed in the right half of the universe.")

        add_seed_to_universe(seed, universe, (int(x), int(y)), 2)
        print(universe)
        print("Number_red = ", number_red)
        print("Number_blue = ", number_blue)
        check = inquirer.prompt({inquirer.Confirm(
            'confirmed', message="Do you want to continue placing seeds ?", default=True), })["confirmed"]
        if check == False:
            break
    return number_red, number_blue
