#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science  -> Backend  -> Flask  -> Advanced application configuration
Topic name: Advanced responses
Question name: Writing a redirector
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
    from flask import Flask, redirect
    
    app = Flask('main')
    
    url = input() # your code here
    
    @app.route(url)
    def view_function():
        return "Haha! I'm out of reach!"
    
    @app.route('/just/redirect/me')
    def redirector_func():
        redirect(url)
    # -=- ANSWER CODE END -=-


input_ = []
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """
Sample Input 1:

/out/of/breach

Sample Output 1:

correct
"""
