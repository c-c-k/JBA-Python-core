#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science -> Programming languages -> Python -> Working with data -> Data types and operations -> Bytes
Topic name: Bytes basics
Question name: Ord() application
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
    print(sum(ord(char) for char in (input() for _ in range(2))))

    # -=- ANSWER CODE END -=-


input_ = ['a\nb']
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """
Sample Input 1:

a
b

Sample Output 1:

195
"""
