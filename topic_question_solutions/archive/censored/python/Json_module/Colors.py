#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science  -> Programming languages  -> Python  -> Python libraries  -> Networking
Topic name: Json module
Question name: Colors
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
    import json
    
    
    colors = {"rainbow": ["red", "orange", "yellow", "green", "blue", "indigo", "violet"],
              "CMYK": ["cyan", "magenta", "yellow", "key color"],
              "RBG": ["red", "blue", "green"]}
    
    # write your code here
    with open('colors.json', 'w') as file:
        json.dump(colors, file)
    # -=- ANSWER CODE END -=-


input_ = []
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """

"""
