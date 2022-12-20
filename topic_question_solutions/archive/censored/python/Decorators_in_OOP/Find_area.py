#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science  -> Programming languages  -> Python  -> Object -> Advanced  -> OOP
Topic name: Decorators in OOP
Question name: Find area
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
    class Area:
    
        def __init__(self, figure_name):
            self.figure_name = figure_name

        @staticmethod
        def rhombus_area(a, b):
            return (a * b) / 2
    # -=- ANSWER CODE END -=-
    print(Area.rhombus_area(8, 9))


input_ = []
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """

"""
