#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science  -> Programming languages  -> Python  -> Code quality  -> Testing and debugging
Topic name: Testing user input
Question name: PEP 8 conventions
Question rating: Medium

-=- QUESTION BODY -=-
Question text censored.
-=- QUESTION BODY -=-
"""
# -=- QUESTION SOLUTION -=-
import io
import sys


def main():
    # -=- ANSWER CODE START -=-
    def check_name(name: str):
        if name in 'ILO':
            print("Never use the characters 'l', 'O', or 'I'"
                   " as single-character variable names")
        elif name.islower():
            print("It is a common variable")
        elif name.isupper():
            print("It is a constant")
        else:
            print("You shouldn't use mixedCase")
    # -=- ANSWER CODE END -=-


input_ = []
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """
Sample Input 1:

directoryName

Sample Output 1:

You shouldn't use mixedCase

Sample Input 2:

I

Sample Output 2:

Never use the characters 'l', 'O', or 'I' as single-character variable names
"""
