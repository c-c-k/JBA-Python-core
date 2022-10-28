# -*- coding: utf-8 -*-

"""Summary

Description
"""

# --------------------
# IMPORTS
# --------------------
# Standard library modules:
from typing import NamedTuple

# Local scripts and modules:
import strings_handler
from miscellaneous_definitions import COMMENT_STARTER_TOKEN

# --------------------
# TYPES
# --------------------
Index = int | None


# --------------------
# DATA TYPES
# --------------------
class LineInfo(NamedTuple):
    file_path: str
    line_num: int


# --------------------
# CONSTANTS
# --------------------


# --------------------
# CLASSES
# --------------------
class _LineElement:
    __slots__ = ["start_index", "end_index", "text", "length"]

    def __init__(self):
        self.start_index: Index
        self.end_index: Index
        self.text: str
        self.length: int


class _LineElementIndent(_LineElement):
    def __init__(self, line_full_text: str):
        super().__init__()
        self._set_length(line_full_text)
        self.start_index = 0 if self.length > 0 else None
        self.end_index = self.length or None
        self._set_text(line_full_text)

    def _set_length(self, line_full_text: str):
        self.length = len(line_full_text) - len(line_full_text.lstrip())

    def _set_text(self, line_full_text: str):
        self.text = (None if self.end_index is None
                     else line_full_text[:self.end_index])


class _LineElementComment(_LineElement):
    def __init__(self, line_full_text: str):
        super().__init__()
        self._set_start_index(line_full_text)
        self.end_index = len(line_full_text) if self.start_index is not None else None
        self._set_length()
        self._set_text(line_full_text)

    def _set_start_index(self, line_full_text: str):
        # NOTE: The find function should return None if there is no
        #       out of string comment opening token.
        self.start_index = (
            strings_handler.find_first_out_of_string_token_index(
                line_full_text, COMMENT_STARTER_TOKEN))

    def _set_length(self):
        self.length = (self.end_index - self.start_index
                       if self.start_index is not None
                       else 0)

    def _set_text(self, line_full_text: str):
        self.text = (line_full_text[self.start_index:]
                     if self.start_index is not None
                     else None)


class _LineElementCode(_LineElement):
    def __init__(self,
                 line_full_text: str,
                 line_element_indent: _LineElementIndent | None,
                 line_element_comment: _LineElementComment | None
                 ):
        # NOTE: Unlike _LineElementComment and _LineElementIndent,
        #       _LineElementCode does not implicitly handle
        #       empty and blank lines.
        super().__init__()
        self._set_start_and_end_indexes(
            line_full_text, line_element_indent, line_element_comment)
        self._set_length()
        self.text = line_full_text[self.start_index:self.end_index]

    def _set_start_and_end_indexes(
            self, line_full_text, line_element_indent, line_element_comment):
        if line_element_indent is not None and line_element_comment is not None:
            # Line is indented and contains a comment.
            if line_element_indent.end_index == line_element_comment.start_index:
                # An indented comment line without any code.
                self.start_index = None
                self.end_index = None
            else:
                # An indented code line with an inline comment.
                self.start_index = line_element_indent.end_index
                self.end_index = line_element_comment.start_index
        elif line_element_indent is not None:
            # An indented code line without a comment.
            self.start_index = line_element_indent.end_index
            self.end_index = len(line_full_text)
        elif line_element_comment is not None:
            # An unindented code line with an inline comment.
            self.start_index = 0
            self.end_index = line_element_comment.start_index
        else:
            # An unindented code line with no comment.
            self.start_index = 0
            self.end_index = len(line_full_text)

    def _set_length(self):
        self.length = (self.end_index - self.start_index
                       if self.start_index is not None
                       else 0)

    def _set_text(self, line_full_text: str):
        self.text = (line_full_text[self.start_index:self.end_index]
                     if self.length > 0
                     else None)


class Line:
    __slots__ = [
        "text", "text_length",
        "is_empty", "is_blank", "indent", "code", "comment"
    ]

    def __init__(self, line_text: str):
        # NOTE: The order of calls is extremely important.
        self.text = line_text.rstrip("\n")
        # print("line.py 138 ::", [self.text])
        self.text_length: int = 0
        self.is_empty: bool = len(self.text) == 0
        self.is_blank: bool = False
        self.indent: _LineElementIndent | None = None
        self.code: _LineElementCode | None = None
        self.comment: _LineElementComment | None = None
        self._handle_blank_line()
        if not (self.is_empty or self.is_blank):
            self._handle_line_elements()

    def _handle_blank_line(self):
        if len(self.text.strip()) == 0:
            # Line is blank (contains only spaces and tabs)
            self.is_blank = True
            self.text_length = len(self.text)

    @staticmethod
    def _new_element(line_element: _LineElement) -> _LineElement | None:
        # Can't think of the right function name.
        # This doesn't init or create elements but checks if they
        # actually contain some text and sets them to None if they don't.
        if line_element.length > 0:
            return line_element
        else:
            return None

    def _handle_line_elements(self):
        line_element = _LineElementIndent(self.text)
        self.indent = self._new_element(line_element)
        line_element = _LineElementComment(self.text)
        self.comment = self._new_element(line_element)
        line_element = _LineElementCode(self.text, self.indent, self.comment)
        self.code = self._new_element(line_element)

# --------------------
# FUNCTIONS
# --------------------
