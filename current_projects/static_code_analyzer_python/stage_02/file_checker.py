# -*- coding: utf-8 -*-

"""Summary

Description
"""

# --------------------
# IMPORTS
# --------------------
# Standard library modules:
from typing import List, Dict, TextIO, NamedTuple

# Third party modules:

# Local scripts and modules:
import issues
from issues import IssueIds
from line import Line

# --------------------
# TYPES
# --------------------
Index = int | None
IssuesList = List["IssueEntry"] | None
IssueTestResults = Dict[IssueIds, bool]


# --------------------
# DATA TYPES
# --------------------
class IssueEntry(NamedTuple):
    line_num: int
    issue_id: "IssueIds"


# --------------------
# CLASSES
# --------------------
class PEP8FileStyleChecker:
    __slots__ = [
        "_file_issues_list", "_line_issue_test_results",
        "_line", "_line_num", "_line_text", "_empty_line_count"
    ]

    def __init__(self):
        self._line: Line = Line("")
        self._line_num: int = 0
        self._line_text: str = ""
        self._empty_line_count: int = 0
        self._file_issues_list: IssuesList = []
        self._line_issue_test_results: IssueTestResults = {}

    def check_file(self, file: TextIO):
        self._reset()
        for line_text in file:
            self._line_text = line_text
            self._check_line()
            self._update_file_issues()

    def _reset(self):
        self._file_issues_list: IssuesList = []
        self._line_num = 0
        self._empty_line_count = 0

    def _update_file_issues(self):
        line_issues_list = []
        for issue_id, test_positive in self._line_issue_test_results.items():
            if test_positive:
                line_issues_list.append(IssueEntry(self._line_num, issue_id))
        self._file_issues_list.extend(line_issues_list)

    def get_file_issues(self) -> IssuesList:
        if len(self._file_issues_list) > 0:
            return self._file_issues_list
        return None

    def _check_line(self):
        self._line_num += 1
        self._line_issue_test_results: IssueTestResults = {}
        self._line = Line(self._line_text)
        line = self._line
        if line.is_empty:
            self._do_empty_line_checks()
        elif line.is_blank:
            self._do_blank_line_checks()
        else:
            self._do_line_general_checks()
            if line.code is not None:
                self._do_line_code_checks()
            if line.comment is not None:
                self._do_line_comment_checks()
            if line.code is not None and line.comment is not None:
                self._do_line_code_with_comment_checks()
        # Reset empty line count since non-empty line was checked.
            self._empty_line_count = 0

    def _do_empty_line_checks(self):
        self._empty_line_count += 1

    def _do_blank_line_checks(self):
        self._empty_line_count += 1
        self._line_issue_test_results[
            IssueIds.S001] = issues.check_issue_s001(self._line)

    def _do_line_general_checks(self):
        self._line_issue_test_results[
            IssueIds.S001] = issues.check_issue_s001(self._line)
        self._line_issue_test_results[
            IssueIds.S002] = issues.check_issue_s002(self._line)

    def _do_line_code_checks(self):
        self._line_issue_test_results[
            IssueIds.S003] = issues.check_issue_s003(self._line)
        self._line_issue_test_results[
            IssueIds.S006] = issues.check_issue_s006(self._empty_line_count)

    def _do_line_comment_checks(self):
        self._line_issue_test_results[
            IssueIds.S005] = issues.check_issue_s005(self._line)

    def _do_line_code_with_comment_checks(self):
        self._line_issue_test_results[
            IssueIds.S004] = issues.check_issue_s004(self._line)

# --------------------
# FUNCTIONS
# --------------------
