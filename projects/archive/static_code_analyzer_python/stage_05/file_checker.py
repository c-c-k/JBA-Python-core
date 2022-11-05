# -*- coding: utf-8 -*-

"""Summary

Description
"""

# --------------------
# IMPORTS
# --------------------
# Standard library modules:

# Third party modules:

# Local scripts and modules:
import ast_quickfix
from issues import IssuesList, IssueChecker
from line import Line, LineInfo

# --------------------
# TYPES
# --------------------
Index = int | None


# --------------------
# DATA TYPES
# --------------------


# --------------------
# CLASSES
# --------------------
class PEP8FileStyleChecker:
    __slots__ = [
        "_line", "_line_num", "_line_text", "_line_info", "_empty_line_count",
        "_file_path", "_issue_checker", "_ast_checker"
    ]

    def __init__(self):
        self._line: Line | None = None
        self._line_info: LineInfo | None = None
        self._issue_checker: IssueChecker | None = None
        self._ast_checker: ast_quickfix.FullTextChecker | None = None
        self._line_num: int | None = None
        self._line_text: str | None = None
        self._empty_line_count: int | None = None
        self._file_path: str | None = None

    def check_file(self, file_path: str):
        self._reset()
        self._file_path = file_path
        with open(self._file_path, 'r') as file:
            for line_text in file:
                self._line_text = line_text
                self._check_line()
            file.seek(0)
            self._ast_checker.check_file_text(
                issue_checker=self._issue_checker,
                file_path=self._file_path, file_text=file.read()
            )

    def _reset(self):
        self._line_num = 0
        self._empty_line_count = 0
        self._issue_checker = IssueChecker()
        self._ast_checker = ast_quickfix.FullTextChecker()

    def _update_line(self):
        self._line = Line(self._line_text)
        self._line_num += 1
        self._line_info = LineInfo(
            file_path=self._file_path,
            line_num=self._line_num,
        )

    def get_file_issues(self) -> IssuesList | None:
        if len(self._issue_checker.issues_list) > 0:
            return self._issue_checker.issues_list
        return None

    def _check_line(self):
        self._update_line()
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
        self._issue_checker.check_issue_s001(self._line_info, self._line)

    def _do_line_general_checks(self):
        self._issue_checker.check_issue_s001(self._line_info, self._line)
        self._issue_checker.check_issue_s002(self._line_info, self._line)

    def _do_line_code_checks(self):
        self._issue_checker.check_issue_s003(self._line_info, self._line)
        self._issue_checker.check_issue_s006(self._line_info, self._empty_line_count)
        self._issue_checker.check_issue_s007(self._line_info, self._line)
        # self._issue_checker.check_issue_s008(self._line_info, self._line)
        # self._issue_checker.check_issue_s009(self._line_info, self._line)

    def _do_line_comment_checks(self):
        self._issue_checker.check_issue_s005(self._line_info, self._line)

    def _do_line_code_with_comment_checks(self):
        self._issue_checker.check_issue_s004(self._line_info, self._line)

# --------------------
# FUNCTIONS
# --------------------
