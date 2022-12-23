#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science  -> Programming languages  -> Python  -> Code quality  -> Code performance
Topic name: Intro to multithreading
Question name: Meet and greet John Doe
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
    from threading import Thread
    import time

    def hello_doe():
        time.sleep(3)
        print('Wait a moment...\nHave a great day!')

    t1 = Thread(target=hello_doe)
    t1.start()
    print('Hello, John Doe!')
    # -=- ANSWER CODE END -=-


input_ = []
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """
Sample Input 1:

Sample Output 1:

Hello, John Doe!
Wait a moment...
Have a great day!
"""
