#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science -> Programming languages -> Python -> Object -> Methods
Topic name: Methods
Question name: Mountain high
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
    class Mountain:
        meter_to_feet = 0.3048

        def __init__(self, name, height):
            self.name = name
            self.height = height
    
        # create convert_height here
        def convert_height(self):
            return self.height / self.meter_to_feet
    # -=- ANSWER CODE END -=-
    mountain = Mountain('test', 1000)
    print(mountain.convert_height())


input_ = []
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """

"""
