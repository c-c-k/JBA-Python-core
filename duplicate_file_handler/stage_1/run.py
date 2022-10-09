#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""DUPLICATE FILE HANDLER - stage 1: Here come the files

Description
"""

# --------------------
# IMPORTS
# --------------------
# Standard library modules:
import argparse
import os


# Third party modules:

# Local scripts and modules:

# --------------------
# CONSTANTS
# --------------------

# --------------------
# CLASSES
# --------------------

class Msg(object):
    """ Container class for query, report and error message subclasses. """

    class Err(object):
        """ Container class for error messages. """
        # Static attribute messages.
        dir_missing = "Directory is not specified"
        # Interactive method messages
        pass

    class Rep(object):
        """ Container class for report messages. """
        # Static attribute messages.
        # Interactive method messages
        pass

    class Ask(object):
        """ Container class for query messages. """
        # Static attribute messages.
        # Interactive method messages
        pass


class DuplicateFileHandler(object):
    """ Description pending for latter stages."""
    __parser = None
    __args = None
    root_dir = None

    def __init__(self):
        self.__init_argparse()
        self.__parse_args()
        self.__set_root_dir()

    def __init_argparse(self):
        self.__parser = argparse.ArgumentParser()
        self.__parser.print_usage = self.__argparse_override
        self.__parser.error = self.__argparse_override
        self.__parser.add_argument("root_dir")

    @staticmethod
    def __argparse_override(*args):
        pass

    def list_tree_files(self):
        if self.root_dir is None:
            print(Msg.Err.dir_missing)
            return
        for root, dirs, files in os.walk(self.root_dir):
            for file in files:
                print(os.path.join(root, file))

    def __parse_args(self):
        self.__args = self.__parser.parse_args()

    def __set_root_dir(self):
        self.root_dir = self.__args.root_dir


# --------------------
# FUNCTIONS
# --------------------

def main():
    duplicate_file_handler = DuplicateFileHandler()
    duplicate_file_handler.list_tree_files()
    pass


# --------------------
# PROGRAM CODE
# --------------------

if __name__ == "__main__":
    main()
