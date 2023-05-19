#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science  -> Programming languages  -> Python  -> Basics  -> Builtins
Topic name: Parallel iteration
Question name: Zip() in for loops
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
    # please do not modify the following code
    interest_rates = [float(x) for x in input().split(',')]
    years = [int(x) for x in input().split(',')]
    loan_principals = [int(x) for x in input().split(',')]

    def total_interest(rate, len_years, principal):
        return int(rate * len_years * principal)

    print(*(
        total_interest(*info)
        for info
        in zip(interest_rates, years, loan_principals)
    ), sep='\n')
    # -=- ANSWER CODE END -=-


input_ = []
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """
Sample Input 1:

0.02, 0.05, 0.04
2, 3, 5
1000, 2000, 1400

Sample Output 1:

40
300
280
"""
