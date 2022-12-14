#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science -> Programming languages -> Python -> Code quality -> Testing and debugging
Topic name: How to read a traceback
Question name: No response
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
    import requests
    from requests.exceptions import InvalidSchema
    
    
    def get_response(url):
        try:
            response = requests.get(url)
            print(response.status_code)
        except InvalidSchema:
            print('No response')
    # -=- ANSWER CODE END -=-


input_ = []
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """
Sample Input 1:

https://google.com

Sample Output 1:

200

Sample Input 2:

htpps://google.com

Sample Output 2:

No response
"""
