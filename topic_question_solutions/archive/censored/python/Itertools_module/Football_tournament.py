#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science -> Programming languages  -> Python  -> Control flow  -> Iterators and generators
Topic name: Itertools module
Question name: Football tournament
Question rating: Medium

-=- QUESTION BODY -=-
Question text censored.
-=- QUESTION BODY -=-
"""
# -=- QUESTION SOLUTION -=-
import io
import sys


def main():
    teams = ['Best-ever', 'Not-so-good', 'Amateurs']
    # -=- ANSWER CODE START -=-
    import itertools
    # the variable 'teams' is already defined
    for game in itertools.combinations(teams, 2):
        print(game)
    # -=- ANSWER CODE END -=-


input_ = []
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """

"""
