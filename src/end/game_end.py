def game_end(number_red: int, number_blue: int) -> int:
    """Contains the winning player's number

    Args:
        number_red (int): number of red soldiers alive on the battlefield
        number_blue (int): number of red soldiers alive on the battlefield

    Returns:
        int: the number of the winner
    """
    if number_red > number_blue:  # Gagnant rouge
        return 1
    elif number_red < number_blue:  # Gagnant bleu
        return 2
    else:  # Match nul, pas de gagnant
        return 0
