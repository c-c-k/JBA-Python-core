#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science  -> Programming languages  -> Python  -> Working with data  -> Collections  -> Tuples
Topic name: Operations with tuple
Question name: Unpacking
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
    # This solution completely misses the point of this exercise,
    # however, creating a swarm of 1 element tuples
    # and then adding them up 1 pair at a time
    # just cringes on my nerves too much.
    def unpack(input_tuple):
        def iter_unpack(packed):
            for item in packed:
                if isinstance(item, tuple):
                    yield from iter_unpack(item)
                else:
                    yield item
        return tuple(iter_unpack(input_tuple))
    # -=- ANSWER CODE END -=-
    hobbies_Adam = ('reading', ('jogging', 'boxing', 'yoga'), 'movies')
    print(unpack(hobbies_Adam))


input_ = []
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """

"""
