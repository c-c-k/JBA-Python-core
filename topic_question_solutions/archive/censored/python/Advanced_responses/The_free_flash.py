#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science  -> Backend  -> Flask  -> Advanced application configuration
Topic name: Advanced responses
Question name: The free flash
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
    from flask import Flask, flash, get_flashed_messages
    
    app = Flask('main')
    
    @app.route('/')
    def main_view():
        flash("It's cold in the graveyard", 'info')
        flash("You don't know whos is behind you.", 'ahtung')
        flash('There is no pain', 'error')
        flash('What are you receiving', 'interest')

        return get_flashed_messages(category_filter='error')
    # -=- ANSWER CODE END -=-


input_ = []
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """

"""
