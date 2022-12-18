#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science -> Programming languages -> Python -> Python libraries -> Networking
Topic name: Socket module
Question name: Connect and send the data
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
    def submit_data(data, client, address):
        client.connect(address)
        client.send(data.encode())
        client.close()

    # -=- ANSWER CODE END -=-


input_ = []
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """

"""
