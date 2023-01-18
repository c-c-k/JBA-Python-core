#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science  -> Backend  -> Flask  -> Working with database
Topic name: Accessing raw DB
Question name: Poor granny
Question rating: Hard

-=- QUESTION BODY -=-
Question text censored.
-=- QUESTION BODY -=-
"""
# -=- QUESTION SOLUTION -=-
import io
import sys


def main():
    import sqlite3
    conn = sqlite3.connect(":memory:")
    # -=- ANSWER CODE START -=-
    cursor = conn.cursor() # Don't rename the cursor
    
    def insert_records(data):
        create_query = """
        CREATE TABLE patients (
        name TEXT,
        status_desc TEXT
        )
        """
        input_query = """
        INSERT INTO patients
        VALUES (?, ?)
        """
        output_query = """
        SELECT *
        FROM patients
        ORDER BY name
        """
        cursor.execute(create_query)
        cursor.executemany(input_query, data)
        output = cursor.execute(output_query).fetchall()
        print(*output, sep='\n')

    # In this task you mustn't close connection to DB.(Due to the checking features)
    # -=- ANSWER CODE END -=-
    insert_records([('Sarah', 'Covid-20'), ('Nick', 'A23N98'), ('Bob', 'Caries')])
    conn.close()


input_ = []
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """

"""
