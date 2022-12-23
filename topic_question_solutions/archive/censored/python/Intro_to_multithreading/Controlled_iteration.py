#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science  -> Programming languages  -> Python  -> Code quality  -> Code performance
Topic name: Intro to multithreading
Question name: Controlled iteration
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
    from threading import Thread
    import time
    
    def num():
        for i in range(1, 6):
            print("The number is: ", i)
            time.sleep(1)
    
    def double_num():
        for i in range(1, 6):
            print("The double of the number is: ", i * 2)
            time.sleep(1)
    
    def square_num():
        for i in range(1, 6):
            print("The square of the number is: ", i ** 2)
            time.sleep(1)
    
    thread_1 = Thread(target=num)
    thread_2 = Thread(target=double_num)
    thread_3 = Thread(target=square_num)

    thread_1.start()
    time.sleep(0.2)
    thread_2.start()
    time.sleep(0.2)
    thread_3.start()
    # -=- ANSWER CODE END -=-


input_ = []
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """

"""
