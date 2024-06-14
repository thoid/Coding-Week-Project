def game_finished(number_red: int, number_blue: int, time: int, iter_max=100) -> bool:
    """True if the game is over

    Args:
        number_red (int): number of red soldiers still alive on the battlefield
        number_blue (int): number of blue soldiers still alive on the battlefield
        time (int): number of iteration already run since the begining of the game
        iter_max (int, optional): the maximum duration of the game. If there is still no winner at this point the game stops anyway. Defaults to 100.

    Returns:
        bool: whether the game is over or not
    """
    # 2 Conditions de fin : mort d'un des joueurs ou dépassement de temps
    return number_red == 0 or number_blue == 0 or time > iter_max
