#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science  -> Programming languages  -> Python  -> Python libraries  -> Time
Topic name: Datetime parsing and formatting
Question name: Day of the week
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
    from datetime import datetime
    
    
    def get_weekday(datetime_obj:datetime):
        return datetime_obj.strftime('%A')
    # -=- ANSWER CODE END -=-


input_ = []
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """
Sample Input 1:

2014-11-08

Sample Output 1:

Saturday

Sample Input 2:

2019-12-31

Sample Output 2:

Tuesday
"""
