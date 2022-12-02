#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science -> Programming languages -> Python -> Object -> Advanced  -> OOP
Topic name: Method overriding
Question name: Robots
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
    class Robot:
        def __init__(self, name, variety):
            self.name = name
            self.variety = variety
            print("Robot")
    
        def get_info(self):
            return "{} is a {} robot".format(self.name, self.variety)
    
    
    class ServiceRobot(Robot):
        def __init__(self, name):
            self.name = "Gorgon the ALMIGHTY!!!"
            super().__init__(name, "service")
    
    
    new_robot = ServiceRobot("Chappi")
    print(new_robot.get_info())
    # -=- ANSWER CODE END -=-


input_ = []
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """

"""
