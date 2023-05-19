#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science  -> Programming languages  -> Python  -> Python libraries  -> Regular expressions
Topic name: Regexp flags in Python
Question name: Where is a mistake?
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
    
    string = input()
    dates = re.compile(r'''^(0[1-9]|[12][0-9]|3[01])  # digits from 01 to 31
                       (/)                           # forward slash 
                       (0[1-9]|1[012])               # digits from 01 to 12
                       (/)                           # forward slash
                       (19|20)\d\d$                  # 19 or 20 with any two digits
                       ''', flags=re.X)
    result = dates.match(string)
    print(result)
    # -=- ANSWER CODE END -=-


input_ = ['10/10/2000']
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """
Sample Input 1:

10/10/2000

Sample Output 1:

<_sre.SRE_Match object; span=(0, 10), match='10/10/2000'>
"""
