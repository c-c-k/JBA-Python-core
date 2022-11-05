#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science -> Programming languages  -> Python  -> Working with data  -> Collections  -> Lists
Topic name: Indexes
Question name: Different alphabets
Question rating: Easy

-=- QUESTION BODY -=-
Question text censored.
-=- QUESTION BODY -=-
"""
# -=- QUESTION SOLUTION -=-
import io
import string
import sys


def main():
    # -=- ANSWER CODE START -=-
    # don't modify the variable below, please
    alphabet = input()
    # put your python code here
    index = 14
    print(alphabet[index])
    # -=- ANSWER CODE END -=-


input_ = ["0123456789" * 3]
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """

"""
