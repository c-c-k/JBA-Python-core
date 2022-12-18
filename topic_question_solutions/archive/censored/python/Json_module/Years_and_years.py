#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science  -> Programming languages  -> Python  -> Python libraries  -> Networking
Topic name: Json module
Question name: Years and years
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
    import json
    
    
    years = {2020: "leap year", 2021: "regular year", 2022: "regular year",
             2023: "regular year", 2024: "leap year"}

    years_json = json.dumps(years, indent=4)
    # -=- ANSWER CODE END -=-
    print(years_json)


input_ = []
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """

"""
