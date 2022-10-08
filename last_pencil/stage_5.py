#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""LAST PENCIL - stage 5:  The right strategy

Description
"""

# --------------------
# IMPORTS
# --------------------
import string

import stage_5_bot as bot

# --------------------
# MESSAGES
# --------------------
PLAYER_NAMES = ("Player", "Bot")
PENCIL_SYMBOL = "|"
MSG_ASK_TOTAL_PENCILS = "How many pencils would you like to use:"
MSG_ASK_FIRST_PLAYER = string.Template(
    "Who will be the first (${NAME_0}, ${NAME_1}):")
MSG_ERR_PENCIL_START_NAN = "The number of pencils should be numeric"
MSG_ERR_PENCIL_START_ZERO = "The number of pencils should be positive"
MSG_ERR_PENCIL_INVALID_MOVE = "Possible values: '1', '2' or '3'"
MSG_ERR_PENCIL_NOT_ENOUGH = "Too many pencils were taken"
MSG_ERR_WRONG_NAME = string.Template(
    "Choose between ${NAME_0} and ${NAME_1}")
REPORT_ACTIVE_PLAYER = string.Template("${NAME}'s turn")
REPORT_WINNER = string.Template("${NAME} won!")

# --------------------
# CONSTANTS
# --------------------
INDEX_PENCILS = 0
INDEX_PLAYER_ID = 1
ID_PLAYER = 0
ID_BOT = 1
VALID_MOVES = ("1", "2", "3")


# --------------------
# PROGRAM START
# --------------------


def init_game_state() -> list:
    """
    Get, validate and initialise the starting parameters of the game.

    Also, reinitialize the bots random seed.
    Invalid parameters are:
        * A string that is not a natural positive number is given
            as the starting number of pencils.
    :return: A list representing the initial game state.
    """

    # Get the initial number of pencils.
    pencils = get_starting_pencils()

    # Determine the first player.
    player_id = get_first_player_id()

    # Reinitialize the bots random seed.
    bot.randomize()

    return [pencils, player_id]


def get_first_player_id() -> int:
    """
    Determine the player that will move first.

    Repeatedly ask the players for the name of the first player to move
    until they provide valid input.
    Print appropriate error messages in case of invalid input.
    Invalid input is a string that is not one of the hardcoded player names.
    :return: An int representing the ID of the first player.
    """
    query_message = MSG_ASK_FIRST_PLAYER.substitute(
        NAME_0=PLAYER_NAMES[0], NAME_1=PLAYER_NAMES[1])
    while True:
        print(query_message)
        player = input()
        if player not in PLAYER_NAMES:
            query_message = MSG_ERR_WRONG_NAME.substitute(
                NAME_0=PLAYER_NAMES[0], NAME_1=PLAYER_NAMES[1])
            continue
        else:
            if player == PLAYER_NAMES[0]:
                player_id = 0
            else:
                player_id = 1
            return player_id


def get_starting_pencils() -> int:
    """
    Get the game's initial number of pencils.

    Repeatedly ask the players for the initial number of pencils
    until they provide valid input.
    Print appropriate error messages in case of invalid input.
    Invalid input is a string that is not a positive integer.
    NOTE: As per the assignment specifications, negative numbers are
            disqualified on account of the '-' character not being a
            digit and thus get the Not A Number error message.
    :return: An int representing the initial number of pencils in the game.
    """
    query_message = MSG_ASK_TOTAL_PENCILS
    while True:
        print(query_message)
        pencils = input()
        if not pencils.isdigit():
            query_message = MSG_ERR_PENCIL_START_NAN
            continue
        pencils = int(pencils)
        if pencils == 0:
            query_message = MSG_ERR_PENCIL_START_ZERO
            continue
        else:
            return pencils


def execute_turn(game_state: list):
    """
    Execute a game turn

    Game turn structure:
        1. Read and validate how many pencils the active player wishes to remove.
        2. Reduce the total number of pencils by the amount given in step 1.
        3. Cycle the active player to the next player.
    Switch turns between the player and the bot.
    :param game_state: A list representing the current game state.
    :return: None
    """
    # Check if it's the players or the bots turn.
    if game_state[INDEX_PLAYER_ID] == ID_PLAYER:
        # Read and validate the number of pencils the player wishes to remove.
        pencils = get_turn_pencils(game_state[INDEX_PENCILS])
    else:
        # Get the number of pencils the bot wishes to remove.
        pencils = bot.make_move(game_state[INDEX_PENCILS])

    # Reduce pencils.
    game_state[INDEX_PENCILS] -= pencils

    # Cycle players.
    if game_state[INDEX_PLAYER_ID] == 0:
        game_state[INDEX_PLAYER_ID] = 1
    else:
        game_state[INDEX_PLAYER_ID] = 0


def get_turn_pencils(current_pencils: int) -> int:
    """
    Get the number of pencils that are to be removed this turn.

    Repeatedly ask the active player for the number of pencils
    they wish to remove until they provide valid input.
    Print appropriate error messages in case of invalid input.
    Invalid inputs are:
        - A string that is not a positive integer.
        - A number that is not within the allowed range of pencils
            to be taken in a single turn.
        - A number that is greater than the remaining number
            of pencils in the game.
    :return: An int representing the number of pencils to be removed this turn.
    """
    while True:
        pencils = input()
        if pencils not in VALID_MOVES:
            print(MSG_ERR_PENCIL_INVALID_MOVE)
            continue
        pencils = int(pencils)
        if pencils > current_pencils:
            print(MSG_ERR_PENCIL_NOT_ENOUGH)
            continue
        else:
            return pencils


def report_winner(game_state: list):
    """
    Print the name of the victor.

    The winner is the player that did not take the last pencil.
    NOTE: This function needs to be in tune with the execute_turn() function.
            Since the execute_turn function cycles the players after removing
            the pencils for the player who took the last pencil,
            the player that is currently active according to the game state
            is the winner.
    :param game_state:
    :return: None
    """
    print(REPORT_WINNER.substitute(
        NAME=PLAYER_NAMES[game_state[INDEX_PLAYER_ID]]))


def report_game_state(game_state: list):
    """
    Print the current game state.

    :param game_state: A list representing the current game state.
    :return: None
    """
    print(game_state[INDEX_PENCILS] * PENCIL_SYMBOL)
    print(REPORT_ACTIVE_PLAYER.substitute(
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

    report_winner(game_state)


if __name__ == "__main__":
    try:
        run()
    except EOFError:
        print('<EARLY TERMINATION>')
