#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Summary

Description
"""

# --------------------
# Imports
# --------------------
# Standard library modules:

# Third party modules:

# Local scripts and modules:

# --------------------

# --------------------
# Constants declarations.
# --------------------
VALID_OPERATORS = "+-*/"
MESSAGE_GREET = "Enter an equation\n"
MESSAGE_BAD_INPUT = "This is not a poetry class;>"
MESSAGE_BAD_OPERAND = "Do you even know what numbers are? Stay focused!"
MESSAGE_BAD_OPERATOR = ("Yes ... an interesting math operation."
                        " You've slept through all classes, haven't you?")

# --------------------

# --------------------
# Program code
# --------------------
while True:
    # Read test expression from input and split it into tokens.
    tokens = input(MESSAGE_GREET).split()

    # Verify that the correct number of tokens has been entered.
    # NOTE: This is not part of the stage assignment requirement
    #       but seems like a reasonable check and is trivial to do.
    if len(tokens) != 3:
        print(MESSAGE_BAD_INPUT)
        continue

    # Define, validate and convert operand tokens.
    # NOTE: While it is unlikely, it is feasible that
    #       integer and float operands would require different
    #       treatment later on, therefore, an attempt is made to
    #       cast each operand into an integer before attempting
    #       to cast it into a float.
    operands = []
    for i in [0, 2]:
        try:
            operands.append(int(tokens[i]))
        except ValueError:
            try:
                operands.append(float(tokens[i]))
            except ValueError:
                operands = None
                break
    if not operands:
        print(MESSAGE_BAD_OPERAND)
        continue

    # Define and validate operator token.
    operator = tokens[1]
    if operator not in VALID_OPERATORS:
        print(MESSAGE_BAD_OPERATOR)
        continue

    break  # Input validation while loop.
