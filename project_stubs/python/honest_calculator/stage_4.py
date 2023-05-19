#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" "Honest Calculator"

This script emulates a simple calculator with a twist,
it gives you snarky comments for attempting certain calculations.
The things for which you'll get criticised are:
  * Supplying operands that are not integers, floats or "M" (see usage note).
  * Supplying an operator that is not one of "+-*/".
  * Trying to divide by zero.
  * Doing a calculation with only single digit integers.
  * Multiplying by 1.
  * Adding, subtracting or multiplying by 0.
USAGE NOTE:
  Like common simple calculators, the "Honest Calculator" lets you
  store the result of a calculation into memory, to access the stored
  result in a following calculation input "M" instead
  of one of both of the operands.
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
MESSAGE_BAD_INPUT = "This is not a poetry class;>"
MESSAGE_BAD_OPERAND = "Do you even know what numbers are? Stay focused!"
MESSAGE_BAD_OPERATOR = ("Yes ... an interesting math operation. "
                        "You've slept through all classes, haven't you?")
MESSAGE_CONTINUE = "Do you want to continue calculations? (y / n):"
MESSAGE_LAZY_PREFIX = "You are"
MESSAGE_LAZY_1 = " ... lazy"
MESSAGE_LAZY_2 = " ... very lazy"
MESSAGE_LAZY_3 = " ... very, very lazy"
MESSAGE_GREET = "Enter an equation\n"
MESSAGE_STORE_MEMORY = "Do you want to store the result? (y / n):"
MESSAGE_ZERO_DIVISION = "Yeah... division by zero. Smart move..."
TOKENS_NUM = 3
TOKENS_OPERAND_INDEXES = [0, 2]
TOKENS_OPERATOR_INDEX = 1
VALID_OPERATORS = "+-*/"


# --------------------

# --------------------
# Program code
# --------------------
def _get_input_tokens() -> list:
    """
     Read, parse into tokens and do initial validation for user input.


    Read an expression from input, split it into tokens
    and verify that the correct number of tokens has been entered.
    NOTE: This later check is not part of the stage assignment
          requirement but seems like a reasonable check
          and is trivial to do.
    :return: A list containing the split tokens
             or None if the number of tokens is incorrect.
    """
    tokens = input(MESSAGE_GREET).split()
    return tokens if len(tokens) == TOKENS_NUM else None


def _get_operands(memory: float, tokens: list) -> list:
    """
    Validate and cast or read from memory the operands.

    If either of the string operand tokens equals "M" read the value
    of that operand from memory, otherwise try to cast that operands
    string token value into a float.
    :param tokens: A list containing the string tokens.
    :return: A list containing the float operands for the expression
              if the base tokens are valid and None otherwise.
    """
    try:
        operands = [(memory if tokens[i] == "M"
                     else float(tokens[i]))
                    for i in TOKENS_OPERAND_INDEXES]
    except ValueError:
        operands = None
    return operands


def _get_operator(tokens: list) -> str:
    """
    Validate operator token.

    :param tokens: A list containing the string tokens.
    :return: A string containing the operator for the arithmetic expression
              or None if the token for it is not a valid.
    """
    return (tokens[TOKENS_OPERATOR_INDEX]
            if tokens[TOKENS_OPERATOR_INDEX] in VALID_OPERATORS
            else None)


def _get_laziness(operands: list, operator: str) -> str | None:
    """
    Generate and print a message describing the user's "laziness".

    The users laziness is measure by how easy it would have been
      to do the calculation on their own instead
      of using the "Honest Calculator".
    For an expression that only has single digit integer operands
      the user is deemed lazy.
    For a multiplication by 1 the user is deemed very lazy.
    For an addition, subtraction or multiplication by 0
      the user is deemed to be extremely lazy.
    In case the user meets more than one condition
      the laziness messages are cumulative.
    :param operands: A list containing the operands for the expression.
    :param operator: A string containing the operator for the expression.
    :return: A string representing the user's cumulative laziness.
    """
    laziness = "".join([
        MESSAGE_LAZY_1 if _is_single_digits(operands) else "",
        MESSAGE_LAZY_2 if _is_multiply_1(operands, operator) else "",
        MESSAGE_LAZY_3 if _is_non_division_zero(operands, operator) else "",
    ])
    return "".join([MESSAGE_LAZY_PREFIX, laziness]) if laziness else ""


def _is_single_digits(operands: list) -> bool:
    """
    Check if both operands are single digit integer numbers.

    :param operands: A list containing the operands for the expression.
    :return: True if both operands are single digit integer numbers,
              False otherwise.
    """

    def _is_single_digit(operand: float) -> bool:
        return operand.is_integer() and (-10.0 < operand < 10.0)

    return _is_single_digit(operands[0]) and _is_single_digit(operands[1])
    pass


def _is_multiply_1(operands: list, operator: str) -> bool:
    """
    Check if one of the operands is 1 and the operator is "*"

    :param operands: A list containing the operands for the expression.
    :param operator: A string containing the operator for the expression.
    :return: True if one of the operands is 1
              and the operator is "*", False otherwise.
    """
    return (operands[0] == 1 or operands[1] == 1) and operator == "*"


def _is_non_division_zero(operands: list, operator: str) -> bool:
    """
    Check if one of the operands is 0 and the operator is one of "+-*"

    :param operands: A list containing the operands for the expression.
    :param operator: A string containing the operator for the expression.
    :return: True if one of the operands is 0
              and the operator is one of "+-*", False otherwise.
    """
    return (operands[0] == 0 or operands[1] == 0) and operator in "+-*"


def _calculate_expression(operands: list, operator: str) -> float | None:
    """
    Calculate the result of the expression.

    Calculate the result of the expression "operand1 operator operand2"
    And handle division by zero if relevant.
    :param operands: A list containing the operands for the expression.
    :param operator: A string containing the operator for the expression.
    :return: The result of the expression as a float
              or None in case of division by zero.
    """
    if operator == "*":
        return float(operands[0] * operands[1])
    elif operator == "-":
        return float(operands[0] - operands[1])
    elif operator == "+":
        return float(operands[0] + operands[1])
    else:
        try:
            return float(operands[0] / operands[1])
        except ZeroDivisionError:
            return None


def _ask_store_memory() -> bool:
    """
    Ask the user if they want to store the result to memory.

    Persistently ask the user if they want
    to store the result to memory
    until they reply with either a "y" or a "n".
    :return: True if the user chooses "y" and false if they choose "n".
    """
    while True:
        user_choice = input(MESSAGE_STORE_MEMORY)
        if user_choice == "y":
            return True
        elif user_choice == "n":
            return False
        else:
            continue


def _ask_continue() -> bool:
    """
    Ask the user if they want to do more calculations.

    Persistently ask the user if they want
    to do more calculations
    until they reply with either a "y" or a "n".
    :return: True if the user chooses "y" and false if they choose "n".
    """
    while True:
        user_choice = input(MESSAGE_CONTINUE)
        if user_choice == "y":
            return True
        elif user_choice == "n":
            return False
        else:
            continue


def run():
    memory = 0.0
    while True:  # main run loop
        # Read, parse into tokens and do initial validation for user input.
        tokens = _get_input_tokens()
        if tokens is None:
            print(MESSAGE_BAD_INPUT)
            continue  # main run loop
        # Define, validate and cast operands.
        operands = _get_operands(memory, tokens)
        if operands is None:
            print(MESSAGE_BAD_OPERAND)
            continue  # main run loop
        # Define and validate operator token.
        operator = _get_operator(tokens)
        if operator is None:
            print(MESSAGE_BAD_OPERATOR)
            continue  # main run loop

        # Build and print a message describing
        # the user's "laziness" if relevant.
        laziness_message = _get_laziness(operands, operator)
        if laziness_message:
            print(laziness_message)
        # Calculate and print the result of the expression,
        # handle division by zero if relevant.
        result = _calculate_expression(operands, operator)
        if result is None:
            print(MESSAGE_ZERO_DIVISION)
            continue  # main run loop
        else:
            print(result)

        # Ask the user if they want to store the result to memory
        # and act accordingly.
        if _ask_store_memory():
            memory = result
        # Ask the user if they want to do more calculations
        # and act accordingly.
        if _ask_continue():
            continue  # main run loop
        else:
            break  # main run loop


run()
