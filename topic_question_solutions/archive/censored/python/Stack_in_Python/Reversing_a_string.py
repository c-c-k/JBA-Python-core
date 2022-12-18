#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science  -> Programming languages  -> Python  -> Additional instruments  -> Algorithms and data structures
Topic name: Stack in Python
Question name: Reversing a string
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
    from collections import deque
    n = int(input())
    my_stack = deque(input() for _ in range(n))
    print(*(my_stack.pop() for _ in range(n)), sep='\n')
    # -=- ANSWER CODE END -=-


input_ = ['5', 's', 't', 'a', 'c', 'k', ]
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """
Sample Input 1:

5
s
t
a
c
k

Sample Output 1:

k
c
a
t
s
"""
