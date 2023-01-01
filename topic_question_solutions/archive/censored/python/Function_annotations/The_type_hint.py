#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science -> Programming languages -> Python -> Control flow -> Functions -> Advanced usage
Topic name: Function annotations
Question name: The type hint
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
    def function(birth_year: int, current_year:int) -> int:
        print(function.__annotations__)
        return current_year - birth_year

    # -=- ANSWER CODE END -=-
    function(2, 1)


input_ = []
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """
Sample Input 1:


Sample Output 1:

{'birth_year': <class 'int'>, 'current_year': <class 'int'>, 'return': <class 'int'>}
"""
