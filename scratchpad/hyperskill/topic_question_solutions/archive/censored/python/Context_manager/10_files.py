#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science -> Programming languages -> Python -> Working with data -> Working with files
Topic name: Context manager
Question name: 10 files
Question rating: Medium

-=- QUESTION BODY -=-
Question text censored.
-=- QUESTION BODY -=-
"""
# -=- QUESTION SOLUTION -=-
import io
import sys


def main():
    import os

    os.chdir("/dev/shm")

    # -=- ANSWER CODE START -=-
    def create_file(_file_num: int):
        file_name = f"file{_file_num}.txt"
        with open(file_name, "w") as new_file:
            new_file.write(f"{_file_num}\n")

    max_files = 11

    for file_num in range(1, max_files):
        create_file(file_num)
    # -=- ANSWER CODE END -=-
    print(os.listdir("/dev/shm"))


input_ = []
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """

"""
