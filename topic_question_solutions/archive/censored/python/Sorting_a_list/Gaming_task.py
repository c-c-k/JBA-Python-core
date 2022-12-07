#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science -> Programming languages -> Python -> Working with data -> Collections -> Lists
Topic name: Sorting a list
Question name: Gaming task
Question rating: Easy

-=- QUESTION BODY -=-
Question text censored.
-=- QUESTION BODY -=-
"""
# -=- QUESTION SOLUTION -=-
import io
import sys


def main():
    # -=- ANSWER CODE START -=-
    # the following line reads the list from the input, do not modify it, please
    toys = input().split()

    print(sorted(toys, key=len))
    # -=- ANSWER CODE END -=-


input_ = ["Toby", "Marinet", "Chubby", "Kitty"]
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO(" ".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """
Sample Input 1:

Toby Marinet Chubby Kitty

Sample Output 1:

['Toby', 'Kitty', 'Chubby', 'Marinet']
"""
