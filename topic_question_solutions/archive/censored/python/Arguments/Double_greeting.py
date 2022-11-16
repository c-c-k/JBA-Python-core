#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science -> Programming languages  -> Python  -> Control flow  -> Functions  -> Arguments
Topic name: Arguments
Question name: Double greeting
Question rating: Medium

-=- QUESTION BODY -=-
Question text censored.
-=- QUESTION BODY -=-
"""
# -=- QUESTION SOLUTION -=-
import io
import sys


def main():
    def greeting(first_name, second_name):
        print("Hello,", first_name, "and", second_name)
    # -=- ANSWER CODE START -=-
    # the following lines read names from the input, do not modify it, please
    name_1 = input()
    name_2 = input()

    greeting(name_1, name_2)
    greeting(name_2, name_1)
    # -=- ANSWER CODE END -=-


input_ = ["name1\nname2\n"]
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """
Sample Input 1:

Sid
Nancy

Sample Output 1:

Hello, Sid and Nancy
Hello, Nancy and Sid
"""
