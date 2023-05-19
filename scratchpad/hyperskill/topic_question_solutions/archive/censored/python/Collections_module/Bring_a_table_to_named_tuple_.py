#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science  -> Programming languages  -> Python  -> Working with data  -> Collections  -> Advanced  -> Collections
Topic name: Collections module
Question name: Bring a table to named tuple!
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
    from collections import namedtuple
    Student = namedtuple('Student', 'name, age, department')
    students = [
        Student('Alina', '22', 'linguistics'),
        Student('Alex', '25', 'programming'),
        Student('Kate', '19', 'art'),
    ]
    print(*students, sep='\n')
    # -=- ANSWER CODE END -=-


input_ = []
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """

"""
