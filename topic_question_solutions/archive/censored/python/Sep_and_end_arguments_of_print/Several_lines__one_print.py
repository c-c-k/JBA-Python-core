#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science  -> Programming languages  -> Python  -> Basics  -> Builtins
Topic name: Sep and end arguments of print
Question name: Several lines, one print
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
    line1 = "Night, square, apothecary, lantern,"
    line2 = "Its meaningless and pallid light."
    line3 = "Return a half a lifetime after – "
    line4 = "All will remain. A scapeless rite."
    
    # your one print() statement here
    print(line1, line2, line3, line4, sep='\n')
    # -=- ANSWER CODE END -=-


input_ = []
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """

"""
