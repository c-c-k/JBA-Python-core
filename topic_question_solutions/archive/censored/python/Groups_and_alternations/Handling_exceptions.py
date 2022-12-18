#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science  -> Programming languages  -> Python  -> Python libraries  -> Regular expressions
Topic name: Groups and alternations
Question name: Handling exceptions
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
    
    
    # put your regex in the variable template
    template = "(Value|Name|Type)Error"
    string = input()
    match = re.match(template, string)
    print(match.group(1) if match else None)
    # -=- ANSWER CODE END -=-


input_ = ['KeyError']
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """

"""
