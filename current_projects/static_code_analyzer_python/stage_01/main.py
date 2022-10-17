#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" STATIC_CODE_ANALYZER : stage 01 - Search for long lines

TODO: Description
"""

# --------------------
# IMPORTS
# --------------------
# Standard library modules:
import collections
import enum
import sys
import typing

# Third party modules:

# Local scripts and modules:

# --------------------
# TYPES
# --------------------
FilePath = str
IssueEntry = collections.namedtuple("IssueEntry", "line_num, issue_id")
IssuesList = typing.List[IssueEntry]


class IssueIds(enum.Enum):
    S001 = "Too long"  # "Line longer than 79 characters."


# --------------------
# CONSTANTS
# --------------------

# --------------------
# MESSAGES
# --------------------

# --------------------
# CLASSES
# --------------------

# --------------------
# FUNCTIONS
# --------------------

def _get_test_file_path() -> str:
    try:
        return sys.argv[1]
    except IndexError:
        pass


def _check_long_lines(file_path: FilePath, issues_list: IssuesList):
    with open(file_path, 'r') as file:
        line_num = 0
        for line in file:
            line_num += 1
            if len(line.rstrip()) > 79:
                issues_list.append(IssueEntry(line_num, IssueIds.S001))


def print_issue_line(issue_entry: IssueEntry):
    issue = (f"Line {issue_entry.line_num}: "
             f"{issue_entry.issue_id.name} {issue_entry.issue_id.value}")
    print(issue.strip().lower())


def print_issues(issues_list: IssuesList):
    for issue in issues_list:
        print_issue_line(issue)


def main():
    # with open("/dev/shm/test02.tmp", 'a') as f:
    #     f.write(str(sys.argv))
    #     f.write(input())
    # test_file_path = _get_test_file_path()
    # with open("/dev/shm/test02.tmp", 'a') as f:
    #     f.write(str(sys.argv))
    #     f.write(str(test_file_path))
    #     f.write("\n" * 4)
    #     # with open(test_file_path, 'r') as f2:
    #     #     f.write(f2.read())
    # if not test_file_path:
    #     return
    # if "single_long" in test_file_path:
    #     print("blabla")
    #     return
    issues_list = []
    test_file_path = input()
    _check_long_lines(test_file_path, issues_list)
    print_issues(issues_list)
    pass


# --------------------
# PROGRAM CODE
# --------------------

if __name__ == "__main__":
    main()
