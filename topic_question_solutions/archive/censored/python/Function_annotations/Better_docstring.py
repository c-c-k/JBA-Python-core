#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science -> Programming languages  -> Python  -> Control flow  -> Functions  -> Advanced usage
Topic name: Function annotations
Question name: Better docstring
Question rating: Easy

-=- QUESTION BODY -=-
Question text censored.
-=- QUESTION BODY -=-
"""
# -=- QUESTION SOLUTION -=-
import io
import sys


def main():
    # -=- ANSWER CODE START -=-
    # add annotations for the function addition
    annotation_param_a = "first number"
    annotation_param_b = "second number"
    annotation_result = "result of adding a to b"

    def addition(a: annotation_param_a, b: annotation_param_b) -> annotation_result:
        return a + b
    # -=- ANSWER CODE END -=-
    print(addition.__annotations__)
    print(addition(1, 1))


input_ = []
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """
Sample Input 1:

Sample Output 1:

{'a': 'first number', 'b': 'second number', 'return': 'result of adding a to b'}
"""
