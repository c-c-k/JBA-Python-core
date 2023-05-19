#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science -> Backend -> Flask -> Launching server
Topic name: Requests
Question name: The Black Mesa
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
    from flask import Flask, request
    
    app = Flask('main')
    
    req_map = {
        'POST': 'Successfully authorized!',
        'GET': 'Welcome there!',
        'PUT': 'Successfully published!',
        'CREATE': 'Created a new web page!',
    }

    @app.route('/', methods=req_map.keys())
    def main_view():
        return req_map[request.method]
        
    # -=- ANSWER CODE END -=-


input_ = []
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """

"""
