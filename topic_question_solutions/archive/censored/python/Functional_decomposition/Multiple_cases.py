#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science -> Programming languages -> Python -> Control flow -> Functions -> Advanced usage
Topic name: Functional decomposition
Question name: Multiple cases
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
    def f1(x):
        return x ** 2 + 1

    def f2(x):
        return 1 / x ** 2

    def f3(x):
        return x ** 2 - 1

    def f(x):
        if x <= 0:
            func = f1
        elif 0 < x < 1:
            func = f2
        else:
            func = f3
        return func(x)
    # -=- ANSWER CODE END -=-
    print([f(x) for x in [1, 0.1, -1]])


input_ = []
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """
Sample Input 1:

1

Sample Output 1:

0.0

Sample Input 2:

0.1

Sample Output 2:

99.99999999999999
"""
