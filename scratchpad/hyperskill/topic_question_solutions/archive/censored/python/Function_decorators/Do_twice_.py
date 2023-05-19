#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science -> Programming languages -> Python -> Control flow -> Functions -> Advanced usage
Topic name: Function decorators
Question name: Do twice!
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
    def do_twice(function):
        def wrapper(*args, **kwargs):
            function(*args, **kwargs)
            function(*args, **kwargs)

        return wrapper
    # -=- ANSWER CODE END -=-
    @do_twice
    def a():
        print("hhh")

    a()


input_ = []
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """
Sample Input 1:

Hi!

Sample Output 1:

Hi!
Hi!
"""
