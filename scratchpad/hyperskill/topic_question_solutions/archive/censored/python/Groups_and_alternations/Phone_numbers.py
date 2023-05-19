#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science  -> Programming languages  -> Python  -> Python libraries  -> Regular expressions
Topic name: Groups and alternations
Question name: Phone numbers
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

    string = input()
    template = re.compile(r'\+(\d)\D?(\d{3})\D?(\d{3}(\D?\d\d){2})')
    msg_base = 'Full number: {}\nCountry code: {}\nArea code: {}\nNumber: {}\n'
    match = template.match(string)
    msg = (
        msg_base.format(match.group(0), *match.groups())
        if match
        else 'No match'
    )
    print(msg)
    # -=- ANSWER CODE END -=-


# Full number: +1-234-567-89-00
# Country code: 1
# Area code: 234
# Number: 567-89-00

input_ = ['+1-234-567-89-00']
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """
Sample Input 1:

+1-234-567-89-00

Sample Output 1:

Full number: +1-234-567-89-00
Country code: 1
Area code: 234
Number: 567-89-00
"""
