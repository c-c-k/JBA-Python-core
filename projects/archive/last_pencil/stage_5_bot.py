# -*- coding: utf-8 -*-

"""Summary

Description
"""
# --------------------
# IMPORTS
# --------------------
from random import seed, randint


# --------------------
# MODULE CODE
# --------------------

def optimal_move(pencils: int) -> int:
    """
    Calculate the optimal number of pencil to remove.

    The simple logic of this function relies on the bot having the
    advantage and will be entirely suicidal otherwise.
    :param pencils: An integer representing
            the number of pencils left in the game.
    :return: An integer representing the number of pencils
            the bot chooses to remove in the current turn.
    """
    return (pencils - 1) % 4


def random_move() -> int:
    """
    Choose a random number of pencil to remove.

    :return: An integer representing the number of pencils
            the bot chooses to remove in the current turn.
    """
    return randint(1, 3)


def make_move(pencils: int) -> int:
    """
    Make an optimal or random move.

    Make an optimal move when having the advantage
    and a random one otherwise.
    :param pencils: An integer representing
            the number of pencils left in the game.
    :return: An integer representing the number of pencils
            the bot chooses to remove in the current turn.
    """
    if pencils == 1:
        move = 1
    elif (pencils - 1) % 4 == 0:
        move = random_move()
    else:
        move = optimal_move(pencils)
    print(move)
    return move


def randomize():
    """Reinitialize the bots random seed."""
    seed()
