#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science -> Programming languages -> Python -> Working with data -> Data types and operations -> Objects in  -> Python
Topic name: Identity testing
Question name: Extraterrestrial life
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
    # The parental gene sequences are stored here
    one_ancestor = input()
    other_ancestor = input()
    
    # Calculate the identity of a new alien here
    new_alien = int((id(other_ancestor) + id(one_ancestor)) / 2)
    # -=- ANSWER CODE END -=-


input_ = []
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """

"""
