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
MESSAGE_ZERO_DIVISION = "Yeah... division by zero. Smart move..."

# --------------------

# --------------------
# Program code
# --------------------
while True:  # main run loop
    # Read test expression from input and split it into tokens.
    tokens = input(MESSAGE_GREET).split()

    # Verify that the correct number of tokens has been entered.
    # NOTE: This is not part of the stage assignment requirement
    #       but seems like a reasonable check and is trivial to do.
    if len(tokens) != 3:
        print(MESSAGE_BAD_INPUT)
        continue  # main run loop

    # Define, validate and cast operands.
    # NOTE: In difference to my solution to stage 1, I removed
    #       special handling for integer input since it seems
    #       it would not be necessary.
    try:
        operands = [float(tokens[i]) for i in [0, 2]]
    except ValueError:
        operands = None
    if not operands:
        print(MESSAGE_BAD_OPERAND)
        continue  # main run loop

    # Define and validate operator token.
    operator = tokens[1]
    if operator not in VALID_OPERATORS:
        print(MESSAGE_BAD_OPERATOR)
        continue  # main run loop

    # Calculate the result of the expression,
    # handle division by zero if relevant.
    if operator == "/":
        try:
            result = operands[0] / operands[1]
        except ZeroDivisionError:
            print(MESSAGE_ZERO_DIVISION)
            continue  # main run loop
    elif operator == "*":
        result = operands[0] * operands[1]
    elif operator == "-":
        result = operands[0] - operands[1]
    elif operator == "+":
        result = operands[0] + operands[1]
    else:  # Just in case..
        continue  # main run loop

    # cast the result as float, this shouldn't be necessary as both
    # of the operands are floats, however a future modification might
    # make it possible for the operands to be integer, so, it's better
    # to be prepared.
    result = float(result)

    # Print the result
    print(result)

    break  # main run loop
