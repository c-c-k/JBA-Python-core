#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science  -> Programming languages  -> Python  -> Python libraries  -> Networking
Topic name: BeautifulSoup: working with XML
Question name: Prettification
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
    
    contacts = '<?xml version="1.0" encoding="UTF-8"?><contacts><contact><name>Tyrion Lannister</name><prefix>Work</prefix></contact><contact><name>Jon Snow</name><prefix>Personal</prefix></contact><contact><name>Arya Stark</name><prefix>Personal</prefix></contact><contact><name>Daenerys Targaryen</name><prefix>Work</prefix></contact></contacts>'
    parse_tree = BeautifulSoup(contacts, 'xml')
    print(parse_tree.prettify())
    
    # put your code here
    # -=- ANSWER CODE END -=-


input_ = []
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """

"""
