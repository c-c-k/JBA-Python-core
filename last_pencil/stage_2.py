#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""LAST PENCIL - stage 2: New rules

Description
"""

# --------------------
# MESSAGES
# --------------------
NAME_1 = 'Player1'
NAME_2 = 'Player2'
PENCIL_SYMBOL = '|'
MSG_ASK_NUM_PENCILS = 'How many pencils would you like to use:'
MSG_ASK_ACTIVE_PLAYER = f'Who will be the first ({NAME_1}, {NAME_2}):'
REPORT_ACTIVE_PLAYER = '{NAME} is going first!'

# --------------------
# PROGRAM START
# --------------------

# Ask the players for the number of pencils in the game.
print(MSG_ASK_NUM_PENCILS)
num_pencils = int(input())

# Ask the players who will be the first player to move.
print(MSG_ASK_ACTIVE_PLAYER)
first_player = input()

# Report the current game state.
print(PENCIL_SYMBOL * num_pencils)
print(REPORT_ACTIVE_PLAYER.format(NAME=first_player))

