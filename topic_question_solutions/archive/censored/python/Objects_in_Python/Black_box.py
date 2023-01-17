#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science  -> Programming languages  -> Python  -> Working with data  -> Data types and operations  -> Objects in  -> Python
Topic name: Objects in Python
Question name: Black box
Question rating: Medium

-=- QUESTION BODY -=-
Question text censored.
-=- QUESTION BODY -=-
"""
# -=- QUESTION SOLUTION -=-
import io
import sys


def main():
    def blackbox(_lst): return _lst
    # -=- ANSWER CODE START -=-
    # use the function blackbox(lst) that is already defined
    lst = []
    print(
        'same'
        if blackbox(lst) is lst
        else 'new'
    )
    # -=- ANSWER CODE END -=-


input_ = []
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """

"""
