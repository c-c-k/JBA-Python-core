#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""LAST PENCIL - stage 3: Working on the gameplay

Description
"""

# --------------------
# MESSAGES
# --------------------
PLAYER_NAMES = ("Player1", "Player2")
PENCIL_SYMBOL = "|"
MSG_ASK_TOTAL_PENCILS = "How many pencils would you like to use:"
MSG_ASK_FIRST_PLAYER = "Who will be the first ({NAME_0}, {NAME_1}):"
# MSG_ASK_REMOVE_PENCILS = ""
REPORT_ACTIVE_PLAYER = "{NAME}'s turn"

# --------------------
# CONSTANTS
# --------------------
INDEX_PENCILS = 0
INDEX_PLAYER_ID = 1

# --------------------
# PROGRAM START
# --------------------


def init_game_state() -> list:
    """
    Get and initialise the parameters of the game.

    :return: A list representing the initial game state.
    """
    # Create a list that will hold the game state.
    game_state = [None, None]

    # Ask the players for the total number of pencils in the game.
    print(MSG_ASK_TOTAL_PENCILS)
    game_state[INDEX_PENCILS] = int(input())

    # Ask the players who will be the first player to move.
    print(MSG_ASK_FIRST_PLAYER.format(
        NAME_0=PLAYER_NAMES[0], NAME_1=PLAYER_NAMES[1]))
    first_player_name = input()
    if first_player_name == PLAYER_NAMES[0]:
        game_state[INDEX_PLAYER_ID] = 0
    else:
        game_state[INDEX_PLAYER_ID] = 1
    return game_state


def execute_turn(game_state: list):
    """
    Execute a game turn

    Game turn structure:
        1. Read how many pencils the active player wishes to remove.
        2. Reduce the total number of pencils by the amount given in step 1.
        3. Cycle the active player to the next player.
    :param game_state: A list representing the current game state.
    :return: None
    """
    # Reduce pencils.
    num_pencils = int(input())
    game_state[INDEX_PENCILS] -= num_pencils

    # Cycle players.
    if game_state[INDEX_PLAYER_ID]:
        game_state[INDEX_PLAYER_ID] = 0
    else:
        game_state[INDEX_PLAYER_ID] = 1


def report_game_state(game_state: list):
    """
    Print the current game state.

    :param game_state: A list representing the current game state.
    :return: None
    """
    print(''.ljust(game_state[INDEX_PENCILS], PENCIL_SYMBOL))
    print(REPORT_ACTIVE_PLAYER.format(
        NAME=PLAYER_NAMES[game_state[INDEX_PLAYER_ID]]))


def game_over(game_state: list) -> bool:
    """
    Check the game state for game over condition.

    The game is considered over when the number of remaining
    pencils is 0.
    :param game_state: A list representing the current game state.
    :return: True if the game is over and False otherwise.
    """
    return game_state[INDEX_PENCILS] <= 0


def run():
    # Set the games starting conditions.
    game_state = init_game_state()

    while not game_over(game_state):
        # Report game state:
        report_game_state(game_state)

        # Execute a game turn.
        execute_turn(game_state)


if __name__ == "__main__":
    run()
