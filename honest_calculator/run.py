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
MESSAGE_STORE_MEMORY = "Do you want to store the result? (y / n):"
MESSAGE_CONTINUE = "Do you want to continue calculations? (y / n):"

# --------------------

# --------------------
# Program code
# --------------------
memory = 0
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
        operands = [(memory if tokens[i] == "M" else float(tokens[i])) for i in [0, 2]]
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

    # Query the user if they want to store the result to memory
    # and act accordingly.
    while True:  # Store to memory query loop
        user_choice = input(MESSAGE_STORE_MEMORY)
        if user_choice == "y":
            memory = result
            break  # Store to memory query loop
        elif user_choice == "n":
            break  # Store to memory query loop
        else:
            continue  # Store to memory query loop

    # Query the user if they want to do more calculations
    # and act accordingly.
    continue_calculating = False
    while True:  # Continue calculating query loop
        user_choice = input(MESSAGE_CONTINUE)
        if user_choice == "y":
            continue_calculating = True
            break  # Continue calculating query loop
        elif user_choice == "n":
            break  # Continue calculating query loop
        else:
            continue  # Continue calculating query loop

    if continue_calculating:
        continue  # main run loop
    else:
        break  # main run loop
