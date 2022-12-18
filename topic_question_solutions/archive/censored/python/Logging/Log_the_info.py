#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science  -> Programming languages  -> Python  -> Code quality  -> Testing and debugging
Topic name: Logging
Question name: Log the info
Question rating: Hard

-=- QUESTION BODY -=-
Question text censored.
-=- QUESTION BODY -=-
"""
# -=- QUESTION SOLUTION -=-
import io
import sys


def main():
    # -=- ANSWER CODE START -=-
    import logging
    # initialize the logger
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    console_handler = logging.StreamHandler()
    log_formater = logging.Formatter("%(levelname)s -> %(message)s")
    console_handler.setFormatter(log_formater)
    logger.addHandler(console_handler)

    def hypotenuse(a, b):
        h = round(((a ** 2 + b ** 2) ** 0.5), 2) 
        # call the logger
        message = f"Hypotenuse of {a} and {b} is {h}"
        logger.info(message)
        return h
    # -=- ANSWER CODE END -=-
    val_1 , val_2 = [int(val) for val in input().split()]
    h = hypotenuse(val_1, val_2)


input_ = ['2 5']
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """
Sample Input 1:

2 5

Sample Output 1:

INFO -> Hypotenuse of 2 and 5 is 5.39
"""
