#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science -> Programming languages -> Python -> Basics -> Builtins
Topic name: Map and filter
Question name: Multiplying lists
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
    def my_product(list_1, list_2):
        return list(map(lambda x, y: x * y, list_2, list_1))
    # -=- ANSWER CODE END -=-


input_ = []
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """

"""
