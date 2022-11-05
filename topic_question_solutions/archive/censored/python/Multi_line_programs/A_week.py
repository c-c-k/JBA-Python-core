#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science -> Programming languages  -> Python  -> Basics  -> Simple programs
Topic name: Multi-line programs
Question name: A week
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
    print("Sunday")
    print("")
    print("Monday")
    print("")
    print("Tuesday")
    print("")
    print("Wednesday")
    print("")
    print("Thursday")
    print("")
    print("Friday")
    print("")
    print("Saturday")
    # -=- ANSWER CODE END -=-


input_ = []
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """
Sample Input 1:

Sample Output 1:

Sunday

Monday

Tuesday

Wednesday

Thursday

Friday

Saturday
"""
