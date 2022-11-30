#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science -> Programming languages -> Python -> Code quality -> Testing and debugging
Topic name: Debugging in shell
Question name: Another error
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
    from io import StringIO

    def add_underscores(word_to_modify):
        with StringIO() as new_word_stream:
            new_word_stream.write("_")
            for char in word_to_modify:
                new_word_stream.write(char)
                new_word_stream.write("_")
            return new_word_stream.getvalue()

    word = input()
    print(add_underscores(word))
    # -=- ANSWER CODE END -=-


input_ = ["error"]
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """
Sample Input 1:

error

Sample Output 1:

_e_r_r_o_r_
"""
