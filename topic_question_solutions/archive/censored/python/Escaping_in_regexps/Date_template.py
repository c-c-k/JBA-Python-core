#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science -> Programming languages  -> Python  -> Python libraries  -> Regular expressions
Topic name: Escaping in regexps
Question name: Date template
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
    import re
    
    # birthday of Python 3
    good_string = '03.12.2008'
    bad_string = '03-12-2008'
    template = r'[01]\d\.[01]\d\.(\d{2}){1,2}\Z'
    # -=- ANSWER CODE END -=-
    print(re.match(template, good_string))
    print(re.match(template, bad_string))


input_ = []
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """

"""
