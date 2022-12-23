#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science  -> Programming languages  -> Python  -> Additional instruments  -> Algorithms and data structures
Topic name: Index() and in under the hood
Question name: Name position
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
    # Do not change the list
    name_list = ["John", "Bob", "Mary", "Jane", "Jack"]
    
    def position(names: list, name):
        return names.index(name) if name in names else None

    idx_name = input()
    name_position = position(name_list, idx_name)
    print(
        name_position
        if name_position is not None
        else 'Name not found'
    )
    # -=- ANSWER CODE END -=-


input_ = ['gamp']
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """
Sample Input 1:

John

Sample Output 1:

0
"""
