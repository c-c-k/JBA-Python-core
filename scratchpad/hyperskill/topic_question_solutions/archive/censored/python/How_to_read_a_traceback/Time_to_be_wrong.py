#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science -> Programming languages -> Python -> Code quality -> Testing and debugging
Topic name: How to read a traceback
Question name: Time to be wrong
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
    def print_list(some_list):
        for i in range(len(some_list)):
            num = int(some_list[i])
            if num % 2 == 0:
                print(num)
            if num % 3 == 0:
                print(num % 3)

    # print_list([1, '2', 3, '4'])
    # -=- ANSWER CODE END -=-


input_ = []
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """

"""
