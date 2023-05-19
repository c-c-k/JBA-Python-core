#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science -> Programming languages  -> Python  -> Python libraries  -> Regular expressions
Topic name: Regexp sets and ranges
Question name: Hyphens? Not a problem!
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
    
    # your code here
    word = input()
    pattern = r"\w+-\w+"
    print(bool(re.match(pattern, word)))
    # -=- ANSWER CODE END -=-


input_ = [
    "twenty-one",
    "long-term",
    "co-worker",
    "well-known",
    "twenty one",
    "long term",
    "co worker",
    "well known",
]
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
for _ in range(len(input_)):
    main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """
Sample Input 1:

good-looking

Sample Output 1:

True
"""
