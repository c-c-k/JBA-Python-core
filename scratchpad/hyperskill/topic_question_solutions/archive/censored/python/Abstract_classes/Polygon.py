#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science  -> Programming languages  -> Python  -> Object -> Advanced  -> OOP
Topic name: Abstract classes
Question name: Polygon
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
    from abc import ABC, abstractmethod
    
    
    class EquilateralPolygon(ABC):
        def __init__(self, side):
            self.side = side
    
        @abstractmethod
        def get_area(self):
            ...
    

    class Square(EquilateralPolygon):
        def get_area(self):
            return self.side ** 2
    # -=- ANSWER CODE END -=-
    print(Square(4).get_area())


input_ = []
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """

"""
