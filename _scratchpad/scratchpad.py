# # !/usr/bin/env python3.10
# # -*- coding: utf-8 -*-
# 
# """Scratch pad for Jet Brains Academy topic questions.
# 
# Properly formatting and saving the solutions for the topic practice
# questions
# feels like a waste of time, so instead I decided to use this script for
# copying and pasting and editing the script and then copying the solution to
# solutions_dump.
#

# Odd or even?
# Medium
# 844 users solved this problem. Latest completion was 19 minutes ago.
# 
# There is a function called is_even(). We do not know its code, but we know
# exactly how it works — given an integer, it returns True if the number is
# even, and False if the number is odd. Write tests for this function (use
# assertTrue and assertFalse).
# 
# In this Code Challenge, you do not need to import the module with the
# function in the beginning of the code. To call the function, just type its
# name, is_even().

# ---- code start ----
# tests for the is_even() function
import unittest


def is_even(num):
    return num % 2 == 0


class TestIsEven(unittest.TestCase):
    __doc__: str

    def test_when_output_true(self):
        self.assertTrue(is_even(2))
        self.__doc__ = self.__doc__

    def test_when_output_false(self):
        self.assertFalse(is_even(1))
        self.__doc__ = self.__doc__

    # def __repr__(self):
    #     return str(self.test_when_output_false()) + str(self.test_when_output_true()) + "hello"


if __name__ == '__main__':
    unittest.main()
