#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science  -> Backend  -> Flask  -> Advanced application configuration
Topic name: Error handlers
Question name: The capital city
Question rating: Hard

-=- QUESTION BODY -=-
Question text censored.
-=- QUESTION BODY -=-
"""
# -=- QUESTION SOLUTION -=-
import io
import sys


def main():
    # -=- ANSWER CODE START -=-
    from flask import Flask, abort
    
    app = Flask(__name__)
    
    @app.route("/capital/<country>")
    def capital(country):
    
        capitals_dictionary = {
            "Russia":"Moscow",
            "Ukraine":"Kiev",
            "USA":"Washington"
        }
    
        # your code here checks that the country is on the list, if not, then abort(400)
        if country in capitals_dictionary.keys():
            return capitals_dictionary[country]
        else:
            return abort(404,  'Resource not found')
    # -=- ANSWER CODE END -=-


input_ = []
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """

"""
