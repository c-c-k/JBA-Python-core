#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science -> Programming languages -> Python -> Code quality -> Testing and debugging
Topic name: How to read a traceback
Question name: Many exceptions
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
    import math
    
    def find_sqrt(number):
        try:
            print(math.sqrt(number))
        except TypeError:
            try:
                print(math.sqrt(int(number)))
            except ValueError:
                print('Please pass a number like "5" or 5')
    # -=- ANSWER CODE END -=-


input_ = []
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """
Sample Input 1:

4

Sample Output 1:

2.0

Sample Input 2:

One

Sample Output 2:

Please pass a number like "5" or 5
"""
