#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science -> Programming languages -> Python -> Basics -> Builtins
Topic name: Map and filter
Question name: Analyzing daily temperatures
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
    def celsius_to_fahrenheit(c):
        return ((c + 40) * 1.8) - 40
    
    
    daily_temp_c = [20.5, 19, 15, 25, 27, 30, 31, 29, 26, 21,
                    19, 25, 27.5, 28, 26, 29.5, 31, 27.5, 26, 29,
                    18, 17.5, 17, 16.5, 19, 20, 25, 26.5, 27, 28,
                    20.5, 19, 25, 27.5, 28, 26, 15, 25, 27, 28]
    
    daily_temp_f = list(map(celsius_to_fahrenheit, daily_temp_c))
    
    temp_above_80 = list(filter(lambda x: x > 80, daily_temp_f))
    
    print(len(temp_above_80))
    # -=- ANSWER CODE END -=-


input_ = []
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """

"""
