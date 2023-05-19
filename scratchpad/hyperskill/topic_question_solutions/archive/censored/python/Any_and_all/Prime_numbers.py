#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science  -> Programming languages  -> Python  -> Basics  -> Builtins
Topic name: Any and all
Question name: Prime numbers
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
    def is_prime(num):
        return all(
            num % divider
            for divider
            in range(2, num // 2 + 1)
        )
    prime_numbers = [num for num in range(2, 1001) if is_prime(num)]
    # -=- ANSWER CODE END -=-
    print(prime_numbers)


input_ = []
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """

"""
