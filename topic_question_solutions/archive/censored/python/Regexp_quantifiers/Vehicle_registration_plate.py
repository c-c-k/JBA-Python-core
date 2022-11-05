#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science -> Programming languages  -> Python  -> Python libraries  -> Regular expressions
Topic name: Regexp quantifiers
Question name: Vehicle registration plate
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
    
    
    # put your regex in the variable template
    template = r"^[A-Z]{2} ?\d{2} ?[A-Z]{2} ?\d{4}$"
    # -=- ANSWER CODE END -=-
    print(re.match(template, "AV34DF2343"))
    print(re.match(template, "AV 34 DF 2343"))
    print(re.match(template, "AV34DF2343 and then hello"))
    print(re.match(template, "V34DF234A3"))


input_ = []
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """

"""
