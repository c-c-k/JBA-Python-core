#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science -> Programming languages  -> Python  -> Basics  -> Modules and packages
Topic name: How to read the documentation
Question name: Numeric Types
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
    def some_calculate(a, b):
        print(abs((a % b) - pow(b, a)))
    # -=- ANSWER CODE END -=-
    some_calculate(*map(int, (input(), input())))


input_ = ["2", "3"]
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """
Sample Input 1:

2
3

Sample Output 1:

7
"""
