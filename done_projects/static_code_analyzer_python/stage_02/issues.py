# -*- coding: utf-8 -*-

"""Summary

Description
"""

# --------------------
# IMPORTS
# --------------------
# Standard library modules:
import enum

# Local scripts and modules:
from line import Line
from miscellaneous_definitions import MAX_LINE_LENGTH


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
}


# --------------------
# FUNCTIONS
# --------------------
def get_issue_description(issue_id: IssueIds):
    return ISSUE_DESCRIPTIONS[issue_id]


def check_issue_s001(line: Line) -> bool:
    """ Line is longer than the recommended maximal line length """
    return len(line.text.expandtabs()) > MAX_LINE_LENGTH


def check_issue_s002(line: Line) -> bool:
    """Indentation is not a multiple of four"""
    return (line.indent is not None) and (len(line.indent.text.expandtabs()) % 4 != 0)


def check_issue_s003(line: Line) -> bool:
    """Unnecessary semicolon after a statement"""
    return (line.code is not None) and line.code.text.rstrip().endswith(";")


def check_issue_s004(line: Line) -> bool:
    """Less than two spaces before inline comments"""
    return ((line.code is not None) and (line.comment is not None)
            and not line.code.text.endswith("  "))


def check_issue_s005(line: Line) -> bool:
    """TO DO found"""
    return line.comment is not None and "TODO" in line.comment.text.upper()


def check_issue_s006(preceding_empty_line_count: int) -> bool:
    """More than two blank lines preceding a code line"""
    return preceding_empty_line_count > 2
