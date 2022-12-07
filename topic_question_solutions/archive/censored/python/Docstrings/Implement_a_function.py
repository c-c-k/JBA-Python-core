#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science -> Programming languages -> Python -> Code quality -> Code style
Topic name: Docstrings
Question name: Implement a function
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
    def get_number(num):
        """Return the number one less than the given positive number. 
        If the number is nonpositive, return a string "Enter a positive number!".
    
        Arguments:
        num -- an integer.
        Return values:
        An integer one less than the input number.
        """
        return (
            (num - 1)
            if num > 0
            else
            "Enter a positive number!"
        )

    # -=- ANSWER CODE END -=-
    for test_num in range(-1, 3):
        print(f"{test_num}: {get_number(test_num)}")


input_ = []
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """

"""
