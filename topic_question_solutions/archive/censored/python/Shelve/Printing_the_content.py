#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science  -> Programming languages  -> Python  -> Additional instruments  -> Advanced tools
Topic name: Shelve
Question name: Printing the content
Question rating: Easy

-=- QUESTION BODY -=-
Question text censored.
-=- QUESTION BODY -=-
"""
# -=- QUESTION SOLUTION -=-
import io
import sys


def main():
    import shelve
    # -=- ANSWER CODE START -=-
    lib = shelve.open("/dev/shm/my_library")
    # lib = shelve.open("my_library")
    lib["Twilight Saga"] = ["Twilight", "New Moon", "Eclipse", "Breaking Dawn"]

    print(*(f'{key}: {value}' for key, value in lib.items()), sep='\n')

    lib.close()
    # -=- ANSWER CODE END -=-


input_ = []
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """

"""
