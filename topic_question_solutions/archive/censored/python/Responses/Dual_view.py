#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science -> Backend -> Flask -> Launching server
Topic name: Responses
Question name: Dual view
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
    from flask import Flask, Response
    
    app = Flask('main')
    
    
    @app.route('/data/main_info')
    def view_func1():
        response = Response(
            response="<h1>Hello there, it's me — my own worst enemy!</h1>",
            status=200,
        )
        return response

    
    @app.route('/the_wall')
    def view_func2():
        response = Response(
            response="<h1>Welkommen!</h1>",
            status=200,
        )
        return response
    # -=- ANSWER CODE END -=-


input_ = []
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """

"""
