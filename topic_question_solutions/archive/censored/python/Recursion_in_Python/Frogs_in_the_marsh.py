#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science  -> Programming languages  -> Python  -> Control flow  -> Functions  -> Advanced usage
Topic name: Recursion in Python
Question name: Frogs in the marsh
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
    def number_of_frogs(year):
        if year == 1:
            return 120
        else:
            prev_num_frogs = number_of_frogs(year - 1)
            return (prev_num_frogs - 50) * 2
    # -=- ANSWER CODE END -=-
    print(number_of_frogs(5))


input_ = []
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """
Sample Input 1:

1

Sample Output 1:

120

Sample Input 2:

5

Sample Output 2:

420
"""
