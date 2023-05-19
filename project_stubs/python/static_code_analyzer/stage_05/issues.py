# -*- coding: utf-8 -*-

"""Summary

Description
"""

# --------------------
# IMPORTS
# --------------------
# Standard library modules:
import enum
import re
from typing import List, NamedTuple

# Local scripts and modules:
from line import Line, LineInfo
from miscellaneous_definitions import MAX_LINE_LENGTH

# --------------------
# TYPES
# --------------------
IssuesList = List["IssueEntry"] | None


# --------------------
# DATA TYPES
# --------------------
class IssueEntry(NamedTuple):
    line_info: LineInfo
    issue_id: "IssueIds"
    issue_args: tuple
    issue_kwargs: dict
    # issue_args: tuple | None = None
    # issue_kwargs: dict | None = None


# --------------------
# ENUMS
# --------------------

class IssueIds(enum.Enum):
    S001 = 1
    S002 = 2
    S003 = 3
    S004 = 4
    S005 = 5
    S006 = 6
    S007 = 7
    S008 = 8
    S009 = 9
    S010 = 10
    S011 = 11
    S012 = 12


# --------------------
# CONSTANTS
# --------------------

ISSUE_DESCRIPTIONS = {
    IssueIds.S001: f"Line longer than {MAX_LINE_LENGTH} characters",
    IssueIds.S002: "Indentation is not a multiple of four",
    IssueIds.S003: "Unnecessary semicolon after a statement",
    IssueIds.S004: "Less than two spaces before inline comments",
    IssueIds.S005: "TODO found ",
    IssueIds.S006: "More than two blank lines preceding a code line",
    IssueIds.S007: "Too many spaces after {TYPE}",
    IssueIds.S008: "Class name {NAME} should be written in CamelCase",
    IssueIds.S009: "Function name {NAME} should be written in snake_case",
    IssueIds.S010: "Argument name {NAME} should be written in snake_case",
    IssueIds.S011: "Variable {NAME} should be written in snake_case",
    IssueIds.S012: "The default argument value is mutable",
}


# --------------------
# CLASSES
# --------------------
class IssueChecker:
    __slots__ = ["issues_list"]

    def __init__(self):
        self.issues_list: IssuesList = []

    def add_issue(
            self, line_info: LineInfo, issue_id: IssueIds,
            *args, **kwargs
    ):
        # args = args if len(args) > 0 else None
        # kwargs = kwargs if len(args) > 0 else None
        self.issues_list.append(IssueEntry(
            line_info, issue_id, args, kwargs))

    def check_issue_s001(self, line_info: LineInfo, line: Line):
        """ Line is longer than the recommended maximal line length """
        if len(line.text.expandtabs()) > MAX_LINE_LENGTH:
            self.add_issue(line_info, IssueIds.S001)

    def check_issue_s002(self, line_info: LineInfo, line: Line):
        """Indentation is not a multiple of four"""
        if (line.indent is not None) and (len(line.indent.text.expandtabs()) % 4 != 0):
            self.add_issue(line_info, IssueIds.S002)

    def check_issue_s003(self, line_info: LineInfo, line: Line):
        """Unnecessary semicolon after a statement"""
        if (line.code is not None) and line.code.text.rstrip().endswith(";"):
            self.add_issue(line_info, IssueIds.S003)

    def check_issue_s004(self, line_info: LineInfo, line: Line):
        """Less than two spaces before inline comments"""
        if ((line.code is not None) and (line.comment is not None)
                and not line.code.text.endswith("  ")):
            self.add_issue(line_info, IssueIds.S004)

    def check_issue_s005(self, line_info: LineInfo, line: Line):
        """TO DO found"""
        if line.comment is not None and "TODO" in line.comment.text.upper():
            self.add_issue(line_info, IssueIds.S005)

    def check_issue_s006(self, line_info: LineInfo, preceding_empty_line_count: int):
        """More than two blank lines preceding a code line"""
        if preceding_empty_line_count > 2:
            self.add_issue(line_info, IssueIds.S006)

    def check_issue_s007(self, line_info: LineInfo, line: Line):
        """Too many spaces after function/class keyword"""
        if line.code is None or not (
                line.code.text.startswith("def")
                or line.code.text.startswith("class")
        ):
            return
        match = re.match(
            (
                # Start matching if the lines code element starts with
                # either a class or a function construction declaration.
                # Match only if there are 2 or more spaces after the
                # def/class keyword.
                # Capture the def/class keyword into the TYPE group.
                r"^(?P<TYPE>def|class)"
                r" {2,}"
            ),
            line.code.text)
        if match:
            self.add_issue(line_info, IssueIds.S007, TYPE=match.group("TYPE"))

    def check_issue_s008(self, line_info: LineInfo, line: Line):
        """Class names should be written in CamelCase"""
        if line.code is None or not line.code.text.startswith("class"):
            return
        match = re.match((
            # Start matching only if a line's code element
            # starts with a class declaration.
            r"^class +"  
            # Set up the capture group "NAME" that would capture 
            # the name of the class if it starts with a lower case 
            # letter, or, if it contains an underscore.
            r"(?P<NAME>"
            r"[a-z]\w*"
            r"|"
            r"\w*?_\w*"
            r")"
            # Terminate match with either ":" or "(".
            r"[:(]"
        ), line.code.text)
        if match:
            self.add_issue(line_info, IssueIds.S008, NAME=match.group("NAME"))

    def check_issue_s009(self, line_info: LineInfo, line: Line):
        """Function names should be written in snake_case"""
        if line.code is None or not line.code.text.startswith("def"):
            return
        match = re.match((
            # Start matching only if a line's code element
            # starts with a function construction declaration.
            r"^def +"
            # Set up the capture group "NAME" that would capture 
            # the name of the function if it contains upper case letters.
            r"(?P<NAME>"
            r"\w*?[A-Z]\w*"
            r")"
            # Terminate match with "(".
            r"[(]"
        ), line.code.text)
        if match:
            self.add_issue(line_info, IssueIds.S009, NAME=match.group("NAME"))


# --------------------
# FUNCTIONS
# --------------------
def print_issue_line(issue_entry: IssueEntry, ):
    issue = " ".join((
        f"{issue_entry.line_info.file_path}:",
        f"Line {issue_entry.line_info.line_num}:",
        issue_entry.issue_id.name,
        get_issue_description(issue_entry.issue_id).format(
            *issue_entry.issue_args, **issue_entry.issue_kwargs)
    ))
    print(issue)


def print_issues(issues_list: IssuesList):
    for issue in sorted(issues_list,
                        key=lambda issue_entry:
                        (issue_entry.line_info.file_path,
                         issue_entry.line_info.line_num,
                         issue_entry.issue_id.name)
                        ):
        print_issue_line(issue)


def get_issue_description(issue_id: IssueIds) -> str:
    return ISSUE_DESCRIPTIONS[issue_id]
