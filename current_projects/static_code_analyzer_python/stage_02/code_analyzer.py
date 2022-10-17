#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" STATIC_CODE_ANALYZER : stage 02 - New checks

TODO: Description
"""

# --------------------
# IMPORTS
# --------------------
# Standard library modules:
import sys
# import typing
from typing import List, NamedTuple
from datetime import datetime as dt

# Third party modules:

# Local scripts and modules:
import issues
from issues import IssueIds
from file_checker import PEP8FileStyleChecker

# --------------------
# TYPES
# --------------------
IssuesList = List["IssueEntry"] | None


# --------------------
# DATA TYPES
# --------------------
class IssueEntry(NamedTuple):
    line_num: int
    issue_id: "IssueIds"


# --------------------
# FUNCTIONS
# --------------------

def _get_test_file_path() -> str | None:
    try:
        return sys.argv[1]
    except IndexError:
        return input()


def print_issue_line(issue_entry: IssueEntry, _temp_file):
    issue = (f"Line {issue_entry.line_num}: "
             f"{issue_entry.issue_id.name} "
             f"{issues.get_issue_description(issue_entry.issue_id)}")
    print(issue)
    print(issue, file=_temp_file)


def print_issues(issues_list: IssuesList, _temp_file):
    for issue in sorted(issues_list,
                        key=lambda issue_entry:
                        issue_entry.line_num * 1000
                        + issue_entry.issue_id.value):
        print_issue_line(issue, _temp_file)


def main(_temp_file):
    test_file_path = _get_test_file_path()
    if not test_file_path:
        print("no file", file=_temp_file)
        return
    print("test file :: " + test_file_path, file=_temp_file)
    pep8_file_checker = PEP8FileStyleChecker()
    with open(test_file_path, 'r') as test_file:
        pep8_file_checker.check_file(test_file)
    issues_list = pep8_file_checker.get_file_issues()
    if not issues_list:
        return
    print_issues(issues_list, _temp_file)


# --------------------
# PROGRAM CODE
# --------------------

if __name__ == "__main__":
    with open("/dev/shm/print.tmp" + dt.now().isoformat(), "w") as temp_file:
        temp_file = sys.stdout
        print("starting time : " + dt.now().isoformat(), file=temp_file)
        main(temp_file)
