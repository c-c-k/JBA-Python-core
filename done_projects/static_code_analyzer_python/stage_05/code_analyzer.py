#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" STATIC_CODE_ANALYZER : stage 02 - New checks

TODO: Description
"""
import os
# --------------------
# IMPORTS
# --------------------
# Standard library modules:
import builtins
from datetime import datetime as dt
import sys
# import typing

# Third party modules:

# Local scripts and modules:
import issues
from issues import IssuesList
from file_checker import PEP8FileStyleChecker


# --------------------
# TYPES
# --------------------


# --------------------
# DATA TYPES
# --------------------


# --------------------
# SILLY PRINT HACK FOR THEN THE AUTOMATED TEST FAILS INCOMPREHENSIBLY
# --------------------


def print(*args, print_to_std: bool = True, **kwargs):
    if print_to_std:
        builtins.print(*args, **kwargs)
    builtins.print(*args, file=print_file, **kwargs)


# --------------------
# FUNCTIONS
# --------------------
def _get_test_dir_path() -> str | None:
    print("sysargv :: ", sys.argv, print_to_std=False)
    try:
        return sys.argv[1]
    except IndexError:
        input_value = input()
        print("input value :: ", input_value, print_to_std=False)
        return input_value


def check_file(file_path: str) -> IssuesList:
    if not file_path.endswith(".py"):
        return
    pep8_file_checker = PEP8FileStyleChecker()
    pep8_file_checker.check_file(file_path)
    return pep8_file_checker.get_file_issues()


def check_dir(root_dir_path: str) -> IssuesList:
    issues_list = []
    if os.path.isfile(root_dir_path):
        return check_file(root_dir_path)
    for root, _, files in os.walk(root_dir_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_issues = check_file(file_path)
            if file_issues:
                issues_list.extend(file_issues)
    return issues_list


def main():
    test_path = _get_test_dir_path()
    print("used path for test dir :: ", test_path, print_to_std=False)
    issues_list = check_dir(test_path)
    if not issues_list:
        return
    issues.print_issues(issues_list)


# --------------------
# PROGRAM CODE
# --------------------

if __name__ == "__main__":
    global print_file
    with open("/dev/shm/print.tmp" + dt.now().isoformat(), "w") as temp_file:
        print_file = temp_file
        print("starting time : " + dt.now().isoformat(), print_to_std=False)
        main()
