#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science  -> Backend  -> Flask  -> Advanced application configuration
Topic name: Error handlers
Question name: Writing an error handler
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
    from flask import Flask, render_template
    
    app = Flask(__name__)
    
    @app.errorhandler(404)
    def page_not_found(e):
     return render_template('404.html')

    @app.errorhandler(403)
    def forbidden(e):
        return render_template('403.html')
    # -=- ANSWER CODE END -=-


input_ = []
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """

"""
