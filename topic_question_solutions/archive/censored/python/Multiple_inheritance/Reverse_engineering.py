#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science  -> Programming languages  -> Python  -> Object -> Advanced  -> OOP
Topic name: Multiple inheritance
Question name: Reverse engineering
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
    # create the hierarchy here
    # (<class '__main__.CarBoat'>, <class '__main__.Car'>, <class
    # '__main__.LandVehicle'>, <class '__main__.Boat'>, <class
    # '__main__.WaterVehicle'>, <class '__main__.Vehicle'>, <class 'object'>)
    class Vehicle:
        pass

    class LandVehicle(Vehicle):
        pass

    class Car(LandVehicle):
        pass

    class WaterVehicle(Vehicle):
        pass

    class Boat(WaterVehicle):
        pass

    class CarBoat(Car, Boat):
        pass

    # -=- ANSWER CODE END -=-
    print(CarBoat.mro())


input_ = []
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """

"""
