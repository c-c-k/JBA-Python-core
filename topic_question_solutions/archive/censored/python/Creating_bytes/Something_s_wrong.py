#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science -> Programming languages -> Python -> Working with data -> Data types and operations -> Bytes
Topic name: Creating bytes
Question name: Something's wrong
Question rating: Hard

-=- QUESTION BODY -=-
Question text censored.
-=- QUESTION BODY -=-
"""
# -=- QUESTION SOLUTION -=-
import io
import sys


def main():
    # -=- ANSWER CODE START -=-
    number = int(input())
    bytes_number = number.to_bytes(5, byteorder='little')
    number_from_bytes = int.from_bytes(bytes_number, 'little')
    print(number == number_from_bytes)  # <-- expected to be True!
    # -=- ANSWER CODE END -=-


input_ = ['0']
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """
Sample Input 1:

0

Sample Output 1:

True
"""
