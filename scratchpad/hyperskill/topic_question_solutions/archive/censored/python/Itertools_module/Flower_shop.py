#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science -> Programming languages  -> Python  -> Control flow  -> Iterators and generators
Topic name: Itertools module
Question name: Flower shop
Question rating: Medium

-=- QUESTION BODY -=-
Question text censored.
-=- QUESTION BODY -=-
"""
# -=- QUESTION SOLUTION -=-
import io
import sys


def main():
    flower_names = ['rose', 'tulip', 'sunflower', 'daisy']
    # -=- ANSWER CODE START -=-
    import itertools
    bouquets = itertools.chain(
        *(itertools.combinations(flower_names, num_flower_types)
            for num_flower_types in range(1, 4)))
    for bouquet in bouquets:
        print(bouquet)
    # -=- ANSWER CODE END -=-


input_ = []
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """

"""
