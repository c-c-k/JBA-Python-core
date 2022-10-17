# -*- coding: utf-8 -*-

"""Summary

Description
"""

# --------------------
# IMPORTS
# --------------------
# Standard library modules:

# Local scripts and modules:
from miscellaneous_definitions import STRING_START_TOKENS

# --------------------
# TYPES
# --------------------
Index = int | None


# --------------------
# CLASSES
# --------------------
class OutOfStringTokenFinder:
    __slots__ = [
        "_test_string", "_search_token", "_current_first_token",
        "_test_start_index", "_current_string_end_index"
    ]

    def __init__(self, test_string: str, search_token: "str"):
        self._test_string: str = test_string
        self._search_token: str = search_token
        self._current_first_token: dict = {"token": "", "index": None}
        self._test_start_index: Index = 0
        self._current_string_end_index: Index = None

    def find_first_index(self) -> Index:
        while True:
            if self._no_search_token_in_substring():
                return None
            self._set_current_first_token()
            if self.first_index_found():
                return self._current_first_token["index"]
            self._update_current_string_end_index()
            self._update_test_start_index()

    def first_index_found(self):
        return self._current_first_token["token"] == self._search_token

    def _set_current_first_token(self):
        self._current_first_token = {
            "token": self._search_token,
            "index": self._test_string.index(
                self._search_token, self._test_start_index)}
        for string_start_token in STRING_START_TOKENS:
            try:
                token_first_index = self._test_string.index(
                    string_start_token, self._test_start_index)
            except ValueError:
                continue
            if token_first_index < self._current_first_token["index"]:
                self._current_first_token = {
                    "token": string_start_token, "index": token_first_index}

    def _update_current_string_end_index(self):
        suspect_end = self._current_first_token["index"] + 1
        while True:
            try:
                suspect_end = self._test_string.index(
                    self._current_first_token["token"], suspect_end)
            except ValueError:
                self._current_string_end_index = None
                return
            if self._test_string[suspect_end - 1] == "\\":
                suspect_end += 1
            else:
                self._current_string_end_index = suspect_end
                return

    def _update_test_start_index(self):
        if self._current_string_end_index is None:
            self._test_start_index = len(self._test_string)
        else:
            self._test_start_index = (
                    self._current_string_end_index
                    + len(self._current_first_token["token"]))

    def _no_search_token_in_substring(self):
        return (self._search_token
                not in self._test_string[self._test_start_index:])


# --------------------
# FUNCTIONS
# --------------------
def find_first_out_of_string_token_index(text_line: str, token: str) -> Index:
    token_searcher = OutOfStringTokenFinder(text_line, token)
    return token_searcher.find_first_index()
