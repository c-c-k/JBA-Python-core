#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" test.py summary

test.py Description
"""


# --------------------
# Imports
# --------------------
# Standard library modules:

# Third party modules:

# Local scripts and modules:
# import _scratchpad

# --------------------
class TestClass:
    """Test class description."""

    def __init__(self, test_param: int):
        """ init doc

        :param test_param:
        """
        self.test_value = test_param

    def test_method(self, param2: float) -> str:
        """ test method doc

        :param param2: param 2 doc
        :return: test method return doc
        """
        return str(param2)


def test_function(param3: bool) -> list:
    """
    test function doc

    :param param3: param 3 doc
    :return: test function return doc
    """
    return [param3]
