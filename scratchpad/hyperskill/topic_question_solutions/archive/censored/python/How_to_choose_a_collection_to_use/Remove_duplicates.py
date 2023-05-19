#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science  -> Programming languages  -> Python  -> Working with data  -> Collections  -> Advanced  -> Collections
Topic name: How to choose a collection to use
Question name: Remove duplicates
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
    names = input().split()
    names = set(names)
    names = sorted(names)
    print(*names, sep='\n')
    # -=- ANSWER CODE END -=-


input_ = ['Jane Mary Jane Tom Alex Sam Alex Sam']
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """
Sample Input 1:

Jane Mary Jane Tom Alex Sam Alex Sam

Sample Output 1:

Alex
Jane
Mary
Sam
Tom
"""
