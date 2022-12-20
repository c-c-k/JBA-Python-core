#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science  -> Programming languages  -> Python  -> Working with data  -> Collections  -> Advanced  -> Collections
Topic name: Collections module
Question name: Food market
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
    from collections import ChainMap
    
    
    food_types = {'Vegetables': 15, 'Dairy': 20, 'Meat': 3, 'Cereals': 9, 'Fruits': 11, 'Fish': 7}
    countries = {'USA': 25, 'Australia': 15, 'Canada': 15, 'France': 6, 'India': 4}
    discount = {'gold': 20, 'regular': 10}
    
    chain = ChainMap(food_types, countries)
    food_types['Sweets'] = 10
    countries['USA'] += 10
    chain = chain.new_child(discount)
    
    # some missing lines
    
    print(chain)
    # -=- ANSWER CODE END -=-


input_ = []
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """

"""
