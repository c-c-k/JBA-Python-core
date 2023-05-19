#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science  -> Programming languages  -> Python  -> Python libraries  -> Regular expressions
Topic name: Regexp flags in Python
Question name: Looking for specific strings
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
    matcher = re.compile('^b.+l$', flags= re.S | re.I)
    match = matcher.match(string)
    print(match.group() if match else 'No match')
    # your code here
    # -=- ANSWER CODE END -=-


input_ = ['base\nball ball']
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """
Sample Input 1:

base\nball ball

Sample Output 1:

base\nball ball
"""
