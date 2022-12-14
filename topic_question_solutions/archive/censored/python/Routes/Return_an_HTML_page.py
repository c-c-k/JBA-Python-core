#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science -> Backend -> Flask -> Launching server
Topic name: Routes
Question name: Return an HTML page
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
    
    app = Flask('main')
    app.app_context()
    
    @app.route('/help')
    def help_route():
        return render_template('help.html')
    
    @app.route('/info')
    def info_route():
        return render_template('info.html')

    # -=- ANSWER CODE END -=-


input_ = []
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """

"""
