#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science  -> Programming languages  -> Python  -> Code quality  -> Code style
Topic name: The pprint module
Question name: Compress it
Question rating: Medium

-=- QUESTION BODY -=-
Question text censored.
-=- QUESTION BODY -=-
"""
# -=- QUESTION SOLUTION -=-
import io
import sys


def main():
    # cars = [
    #     ['Audi A4', 'Audi A7'], ['Nissan Pathfinder', 'Nissan Rogue'],
    #     ['BMW 328i', 'BMW M3'], ['Toyota Camry', 'Toyota Prius']]
    cars = [list(input().split(',')) for _ in range(4)]
    # -=- ANSWER CODE START -=-
    from pprint import pprint
    pprint(cars, compact=True, width=88)

    # -=- ANSWER CODE END -=-


input_ = [
    'Audi A4,Audi A7',
    'BMW 328i,BMW M3',
    'Nissan Pathfinder,Nissan Rogue',
    'Toyota Camry,Toyota Priu',
]
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """
Sample Input 1:

Audi A4,Audi A7
BMW 328i,BMW M3
Nissan Pathfinder,Nissan Rogue
Toyota Camry,Toyota Priu

Sample Output 1:

[['Audi A4', 'Audi A7'], ['BMW 328i', 'BMW M3'], ['Nissan Pathfinder', 'Nissan Rogue'],
 ['Toyota Camry', 'Toyota Priu']]
"""
