#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science  -> Programming languages  -> Python  -> Python libraries  -> Regular expressions
Topic name: Preconditions and postconditions
Question name: HTML lists? No problem!
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
    template = r'(?<=<li>).+?(?=</li>)'
    print(*re.findall(template, string), sep='\n')
    # -=- ANSWER CODE END -=-


input_ = []
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_), sep='\n')
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """
Sample Input 1:

<li>Sister</li> <li>Father</li> <li>Mother-in-law</li>

Sample Output 1:

Sister
Father
Mother-in-law
"""
