#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science  -> Programming languages  -> Python  -> Python libraries
Topic name: Delete data with SQLite
Question name: A clean sweep
Question rating: Medium

-=- QUESTION BODY -=-
Question text censored.
-=- QUESTION BODY -=-
"""
# -=- QUESTION SOLUTION -=-
import io
import sys


def main():
    import sqlite3
    conn = sqlite3.connect("")
    cursor = conn.cursor()
    # -=- ANSWER CODE START -=-
    # delete records
    query = """
    DELETE FROM Customers
    WHERE country = ?
    """
    args = ("France",)
    cursor.execute(query, args)
    
    # print the number of affected rows
    print(cursor.rowcount)
    # -=- ANSWER CODE END -=-


input_ = []
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """

"""
