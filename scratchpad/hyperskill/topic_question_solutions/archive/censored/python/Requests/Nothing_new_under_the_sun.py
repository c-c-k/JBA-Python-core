#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science -> Backend -> Flask -> Launching server
Topic name: Requests
Question name: Nothing new under the sun
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
    from flask import request, Flask
    app = Flask('main')

    @app.route('/', methods=['DELETE', 'PUT'])
    def database_manipulator():
        if request.method == 'DELETE':
            return "Deleted"
        elif request.method == 'PUT':
            return "Updated"
    # -=- ANSWER CODE END -=-


input_ = []
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """
Sample Input 1:

DELETE

Sample Output 1:

Deleted
"""
