#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science  -> Programming languages  -> Python  -> Working with data  -> Collections  -> Advanced  -> Collections
Topic name: Defaultdict and Counter
Question name: The mode
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
    from collections import Counter
    data = Counter(input().split())
    print(data.most_common(1)[0][0])

    # -=- ANSWER CODE END -=-


input_ = ['1 7 3 3 8 9 10 5 5 5 4 1 5 6']
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """
Sample Input 1:

1 7 3 3 8 9 10 5 5 5 4 1 5 6

Sample Output 1:

5

Sample Input 2:

red green yellow red orange blue purple

Sample Output 2:

red
"""
