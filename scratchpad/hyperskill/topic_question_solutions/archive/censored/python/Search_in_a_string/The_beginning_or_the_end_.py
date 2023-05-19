#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science  -> Programming languages  -> Python  -> Working with data  -> Data types and operations  -> Strings
Topic name: Search in a string
Question name: The beginning or the end?
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
    string = input()
    indexes = (string.find('old'), string.rfind('old'))
    print(max(indexes))
    # -=- ANSWER CODE END -=-


input_ = ['old macdonald had an old farm']
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """
Sample Input 1:

old macdonald had an old farm

Sample Output 1:

21
"""
