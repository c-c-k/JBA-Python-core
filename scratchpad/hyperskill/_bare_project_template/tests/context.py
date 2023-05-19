#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Adjust $PYTHONPATH context.

This module adjusts the $PYTHONPATH environment variable to make
the tests run in the context of the projects root directory.
This should not be necessary if the tests are run from inside Pycharm
or another advanced IDE like VS-Code.
This is necessary if the tests are run directly from the shell or from
a text editor/simple IDE that does not take care of adjusting $PYTHONPATH
context on its own.
For this module to work, it must be imported into every test module
in the same directory.
For each subdirectory the relative path ("..") needs to be adjusted
i.e. "../.." , "../../.." and so on.
"""

import os.path
import sys

src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if src_path not in sys.path:
    sys.path.insert(0, src_path)
