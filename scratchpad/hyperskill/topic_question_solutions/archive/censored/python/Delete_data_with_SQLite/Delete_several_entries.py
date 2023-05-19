#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science  -> Programming languages  -> Python  -> Python libraries
Topic name: Delete data with SQLite
Question name: Delete several entries
Question rating: Medium

-=- QUESTION BODY -=-
Question text censored.
-=- QUESTION BODY -=-
"""
# -=- QUESTION SOLUTION -=-
import io
import sys


def main():
    from sqlite3 import connect
    conn = connect("")
    cursor = conn.cursor()
    # -=- ANSWER CODE START -=-
    list_of_cities = [(input().strip(),) for _ in range(3)]
    query = """
    DELETE FROM Customers
    WHERE city = ?
    """
    cursor.executemany(query, list_of_cities)
    cursor.close()
    # -=- ANSWER CODE END -=-
    conn.close()


input_ = []
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """
Sample Input 1:

Paris
Seul
Cali

Sample Output 1:

6
"""
