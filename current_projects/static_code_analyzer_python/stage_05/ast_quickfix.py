# -*- coding: utf-8 -*-

"""Summary

Description
"""

# --------------------
# IMPORTS
# --------------------
# Standard library modules:
import ast
import re
import typing

# Third party modules:

# Local scripts and modules:
import issues
import line


# --------------------
# CONSTANTS
# --------------------


# --------------------
# CLASSES
# --------------------
class FullTextChecker(ast.NodeVisitor):
    def __init__(self):
        super(ast.NodeVisitor).__init__()
        self.issue_checker: issues.IssueChecker | None = None
        self.file_path: str | None = None
        self.root_node: ast.Module | None = None

    def add_issue(
            self, line_num: int, issue_id: issues.IssueIds,
            *args, **kwargs
    ):
        self.issue_checker.add_issue(
            line.LineInfo(self.file_path, line_num),
            issue_id, *args, **kwargs)

    def check_file_text(
            self, issue_checker: issues.IssueChecker,
            file_path: str, file_text: str
    ):
        self.issue_checker = issue_checker
        self.file_path = file_path
        try:
            self.root_node = ast.parse(file_text, filename=file_path)
        except (IndentationError, SyntaxError):
            return
        self.visit(self.root_node)

    def visit_ClassDef(self, node: ast.ClassDef) -> typing.Any:
        self.check_issue_008(node)
        self.generic_visit(node)

    def check_issue_008(self, node: ast.ClassDef):
        """Class names should be written in CamelCase"""
        class_name = get_name_non_camel_case(node.name)
        if class_name is not None:
            self.add_issue(node.lineno, issues.IssueIds.S008, NAME=class_name)

    def visit_FunctionDef(self, node: ast.FunctionDef) -> typing.Any:
        self.check_issue_009(node)
        self.check_issue_010(node)
        self.check_issue_011(node)
        self.check_issue_012(node)
        self.generic_visit(node)

    def check_issue_009(self, node: ast.FunctionDef):
        """Function names should be written in snake_case"""
        function_name = get_name_non_snake_case(node.name)
        if function_name is not None:
            self.add_issue(node.lineno, issues.IssueIds.S009, NAME=function_name)

    def check_issue_010(self, node: ast.FunctionDef):
        """Argument names should be written in snake_case"""
        args = (
                list(node.args.args)
                + list(node.args.posonlyargs)
                + list(node.args.kwonlyargs)
        )
        for arg in args:
            arg_name = get_name_non_snake_case(arg.arg)
            if arg_name is not None:
                self.add_issue(node.lineno, issues.IssueIds.S010, NAME=arg_name)

    def check_issue_011(self, node: ast.FunctionDef):
        """Variable names should be written in snake_case"""
        for sub_node in ast.walk(node):
            if isinstance(sub_node, ast.Assign):
                var_names = []
                for target in list(sub_node.targets):
                    if isinstance(target, ast.Name):
                        var_names.append(target.id)
                    elif isinstance(target, ast.Attribute):
                        var_names.append(target.attr)
                    else:
                        continue
                for var_name in var_names:
                    var_name = get_name_non_snake_case(var_name)
                    if var_name is not None:
                        self.add_issue(sub_node.lineno, issues.IssueIds.S011, NAME=var_name)

    def check_issue_012(self, node: ast.FunctionDef):
        """The default argument value is mutable"""
        defaults = (
                list(node.args.defaults)
                + list(node.args.kw_defaults)
        )
        for default in defaults:
            if not isinstance(default, ast.Constant):
                self.add_issue(node.lineno, issues.IssueIds.S012)
                return


# --------------------
# FUNCTIONS
# --------------------
def get_name_non_snake_case(name: str) -> str | None:
    # Match a name that either doesn't start
    # with a lowercase letter or an underscore,
    # or, a name that contains a capital.
    match = re.match("[^a-z_].*|.+?[^0-9a-z_].*", name)
    return match.group() if match is not None else None


def get_name_non_camel_case(name: str) -> str | None:
    # Match a name that either doesn't start with a capital,
    # or, a name that contains an underscore.
    match = re.match("[^A-Z].*|.+?_.*", name)
    return match.group() if match is not None else None

