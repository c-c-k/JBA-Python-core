#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science  -> Programming languages  -> Python  -> Python libraries  -> Math
Topic name: Float special values
Question name: Declaring variables
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
    # set the special values here
    import math
    pos_inf = float('inf')
    neg_inf = float('-inf')
    nan = float('nan')
    # -=- ANSWER CODE END -=-
    print(*((x, type(x)) for x in (
        nan, pos_inf, neg_inf, math.inf, math.nan
    )))


input_ = []
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """

"""
