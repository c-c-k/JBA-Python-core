#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science -> Backend -> Flask -> Launching server
Topic name: Responses
Question name: The Code Sender
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
    from flask import Flask, jsonify

    app = Flask('main')
    app.app_context()

    @app.route('/<data>')
    def response_maker(data):
        text, status_code = data.split(';')

        # your code here
        return jsonify({"code": status_code, "message": text})
    # -=- ANSWER CODE END -=-


input_ = []
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """
Sample Input 1:

Hello there, my friend!
200

Sample Output 1:

{"code":"200","message":"Hello there, my friend!"}
"""
