#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science  -> Backend  -> Flask  -> Working with database
Topic name: Accessing raw DB
Question name: Question of classification
Question rating: Hard

-=- QUESTION BODY -=-
Question text censored.
-=- QUESTION BODY -=-
"""
# -=- QUESTION SOLUTION -=-
import io
import sys


def main():
    from sqlite3 import connect
    conn = connect(":memory:")
    # -=- ANSWER CODE START -=-
    cursor = conn.cursor()

    update_query = """
    UPDATE patients
    SET disease = 'B36C16'
    WHERE disease = 'A35B15'
    """
    cursor.execute(update_query)


    # In this task you mustn't close connection to DB.(Due to the checking features)
    # -=- ANSWER CODE END -=-


input_ = []
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """

"""
