#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science  -> Programming languages  -> Python  -> Additional instruments  -> Advanced tools
Topic name: Shelve
Question name: Context manager usage
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
    import shelve

    # with shelve.open('my_library') as shelf:
    with shelve.open('/dev/shm/my_library') as shelf:
        shelf['Anna Karenina'] = (
            'Happy families are all alike'
            ' every unhappy family is unhappy in its own way...'
        )
    print('A new book has been added to the library!')
    # -=- ANSWER CODE END -=-
    with shelve.open('/dev/shm/my_library') as shelf:
        print(*shelf.items())


input_ = []
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """

"""
