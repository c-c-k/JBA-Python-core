#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science -> Programming languages  -> Python  -> Control flow  -> Iterators and generators
Topic name: Itertools module
Question name: Restaurant
Question rating: Medium

-=- QUESTION BODY -=-
Question text censored.
-=- QUESTION BODY -=-
"""
# -=- QUESTION SOLUTION -=-
import io
import sys


def main():
    main_courses = ['beef stew', 'fried fish']
    price_main_courses = [28, 23]
    desserts = ['ice-cream', 'cake']
    price_desserts = [2, 4]
    drinks = ['cola', 'wine']
    price_drinks = [3, 10]
    # -=- ANSWER CODE START -=-
    import itertools
    money = 30
    for diner, diner_costs in zip(
        itertools.product(main_courses, desserts, drinks),
        itertools.product(price_main_courses, price_desserts, price_drinks),
    ):
        diner_total_cost = sum(diner_costs)
        if diner_total_cost <= money:
            print(" ".join(diner), diner_total_cost)
    # -=- ANSWER CODE END -=-


input_ = []
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """

"""
