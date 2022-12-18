#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science  -> Programming languages  -> Python  -> Python libraries  -> Regular expressions
Topic name: Preconditions and postconditions
Question name: Posthyphen
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
    import re
    
    string = input()
    template = r'(?<=-)\w+'
    match = re.search(template, string)
    print(match.group())
    # -=- ANSWER CODE END -=-


input_ = ['cat-dog']
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """
Sample Input 1:

cat-dog

Sample Output 1:

dog
"""
