#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science  -> Programming languages  -> Python  -> Python libraries  -> Networking
Topic name: BeautifulSoup: working with XML
Question name: Greek Goddesses
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
    
    goddesses = '<?xml version="1.0" encoding="UTF-8"?> \
    <goddesses> \
      <goddess>Hestia</goddess> \
      <goddess>Hebe</goddess> \
      <goddess>Nemesis</goddess> \
      <goddess>Leto</goddess> \
      <goddess>Rhea</goddess> \
      <goddess>Aphrodite</goddess> \
      <goddess>Demeter</goddess> \
      <goddess>Artemis</goddess> \
      <goddess>Hera</goddess> \
      <goddess>Athena</goddess> \
      <goddess>Cybele</goddess> \
      <goddess>Persephone</goddess> \
      <goddess>Nyx</goddess> \
      <goddess>Selene</goddess> \
      <goddess>Tyche</goddess> \
      <goddess>Maia</goddess> \
      <goddess>Lachesis</goddess> \
      <goddess>Iris</goddess> \
      <goddess>Nike</goddess> \
      <goddess>Keres</goddess> \
    </goddesses>'
    
    # put your code here
    soup = BeautifulSoup(goddesses, 'xml')
    goddesses = soup.find_all('goddess')
    print(*(goddess.text for goddess in goddesses), sep='\n')
    # -=- ANSWER CODE END -=-


input_ = []
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """

"""
