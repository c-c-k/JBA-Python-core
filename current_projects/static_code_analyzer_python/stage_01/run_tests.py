#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Test suit for stage 01 of STATIC_CODE_ANALYZER

TODO: Description
"""
import os.path

# --------------------
# IMPORTS
# --------------------

# Standard library modules:
import os
import io
import sys

# Third party modules:

# Local scripts and modules:
# noinspection PyUnresolvedReferences
import context
import src.stages.stage_01.main as stage_main


# --------------------
# CONSTANTS
# --------------------

# --------------------
# CLASSES
# --------------------
class Test:
    __slots__ = [
        "_test_description", "_has_failed_tests",
        "_test_dataset_root",
        "_test_num", "_num_tests", "_test_finished"
        # "_test_inputs",
        # "_single_args", "_single_kwargs",
        # "_multi_args", "_multi_kwargs",
    ]

    def __init__(self):
        self._test_description = "Base test class"
        self._has_failed_tests = False
        self._test_dataset_root = os.path.join(
            os.path.dirname(__file__), "test_dataset")
        self._test_finished = False
        self._num_tests = 1
        self._test_num = 0
        # self._single_args = []
        # self._single_kwargs = {}
        # self._multi_args = [[]]
        # self._multi_kwargs = [{}]
        pass

    def test(self):
        pass

    def run_tests(self):
        print(f"=== running test: {self._test_description} ===")
        while self._test_num < self._num_tests:
            self._test_num += 1
            try:
                self.test()
            except AssertionError as err:
                print(f"Subtest {self._test_num:d} failed: {err.args[0]}")
                self._has_failed_tests = True
        print("" if self._has_failed_tests else "--- test passed.")


class TestGetFilePath(Test):
    def __init__(self):
        super(TestGetFilePath, self).__init__()
        self._test_description = "Check get filename from system call arguments."
        self.__original_argv = None

    def test(self):
        test_path = "/dev/shm/test"
        self.__original_argv = sys.argv[:]
        sys.argv = [sys.argv[0], test_path]
        stage_path = stage_main._get_test_file_path()
        assert stage_path == test_path, ("Mismatch: "
                                         f"intended path : {test_path} ,"
                                         f" actual path: {stage_path}")


# --------------------
# FUNCTIONS
# --------------------


def main():
    # TestGetFilePath().run_tests()
    argv_original = sys.argv[:]
    sys.argv = [sys.argv[0], ""]
    for root, _, files in os.walk(
            os.path.join(os.path.dirname(__file__), "test_dataset")):
        oldsysstdin = sys.stdin
        for file in files:
            test_file_path = os.path.join(root, file)
            print(test_file_path)
            # sys.argv[1] = test_file_path
            # sys.stdin.buffer.write("asf")
            # with open(sys.stdin.name, 'a') as f:
            #     f.write("heel\n")
            #     f.flush()
            with io.StringIO(test_file_path) as sys.stdin:
                stage_main.main()
    sys.stdin = oldsysstdin
    sys.argv = argv_original
    pass


# --------------------
# PROGRAM CODE
# --------------------

if __name__ == "__main__":
    main()
