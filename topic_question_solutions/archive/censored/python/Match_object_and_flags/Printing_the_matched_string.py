#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science  -> Programming languages  -> Python  -> Python libraries  -> Regular expressions
Topic name: Match object and flags
Question name: Printing the matched string
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
    import re
    day_periods = ("morning", "afternoon", "evening")
    template = fr'(Good ({"|".join(day_periods)}))'

    string = input()
    match = re.match(template, string)
    print(match.group(1) if match else 'No greeting!')
    # -=- ANSWER CODE END -=-


input_ = ['Good mrning fred']
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """
Sample Input 1:

Good morning

Sample Output 1:

Good morning
"""
