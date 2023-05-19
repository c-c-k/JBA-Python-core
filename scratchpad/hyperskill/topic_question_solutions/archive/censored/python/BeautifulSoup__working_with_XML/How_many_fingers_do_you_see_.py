#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science  -> Programming languages  -> Python  -> Python libraries  -> Networking
Topic name: BeautifulSoup: working with XML
Question name: How many fingers do you see?
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
    from bs4 import BeautifulSoup
    
    fingers = '<?xmlversion="1.0"encoding="UTF-8"?><fingers><finger><name>Thumb</name><hand>Left</hand></finger><finger><name>Index</name><hand>Left</hand></finger><finger><name>Index</name><hand>Right</hand></finger><finger><name>Middle</name><hand>Right</hand></finger><finger><name>Little</name><hand>Left</hand></finger></fingers>'
    
    # put your code here
    soup = BeautifulSoup(fingers, 'xml')
    print(sum(1 for _ in soup.find_all('finger')))
    # for finger in soup.find_all('finger'):
    #     print(finger.find('name').text)
    # -=- ANSWER CODE END -=-


input_ = []
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """

"""
