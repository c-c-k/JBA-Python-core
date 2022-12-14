#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science -> Programming languages -> Python -> Control flow -> Functions -> Advanced usage
Topic name: Function decorators
Question name: Math operations
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
    def print_info(func):
        def wrapper(arg1, arg2):
            print("The arguments of the function are:", arg1, arg2)
            return func(arg1, arg2)

        return wrapper


    @print_info
    def addition(arg1, arg2):
        return arg2 + arg1
    # -=- ANSWER CODE END -=-


input_ = []
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """

"""
