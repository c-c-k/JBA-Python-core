#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""DUPLICATE FILE HANDLER - stage 1: Here come the files

Finds and handles duplicate files in the tree of a given root dir.
Stage 1 assignment requirements:
    - Recursively scan the given root dir and it's subdirectories for files.
    - Print the full path of all files found.
"""

# --------------------
# IMPORTS
# --------------------
# Standard library modules:
import argparse
import os

# --------------------
# MESSAGES
# --------------------

MSG_ERR_DIR_MISSING = "Directory is not specified"


# --------------------
# FUNCTIONS
# --------------------

def init_argparse() -> argparse.ArgumentParser:
    """ Setup and Initialize argparse.

    The "print_usage" and "error" methods of the parser are overwritten with
    an empty function to prevent it from printing to standard output messages
    that will confuse the Hyperskill automated assignment checker.
    :return: An argument parser object ready to parse.
    """
    parser = argparse.ArgumentParser()
    parser.print_usage = argparse_error_override
    parser.error = argparse_error_override
    parser.add_argument("root_dir")
    return parser


# noinspection PyUnusedLocal
def argparse_error_override(*args):
    pass


def get_root(parser: argparse.ArgumentParser) -> str | None:
    """Get root dir from argparse."""
    return parser.parse_args().root_dir


def get_tree_files(root_dir: str) -> list:
    """ Create and return a list of all the files
        in the directory tree starting from root_dir. """
    file_list = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list


def print_files(files: list):
    """ Print all the full path of all the files in the files list """
    print(*files, sep="\n")


def main():
    # Setup and Initialize argparse.
    # NOTE: Since the there is only one  argument to be parsed here,
    # using argparse instead of sys.argv() is an overkill
    # and overcomplicates things, however, I'm not sure what the
    # requirements for the next stages are going to be.
    parser = init_argparse()

    # Get root dir from argparse.
    root_dir = get_root(parser)

    # print error message and exit if root dir was not provided.
    if root_dir is None:
        print(MSG_ERR_DIR_MISSING)
        return

    # Create a list of all the files
    # in the directory tree starting from root_dir.
    file_list = get_tree_files(root_dir)

    # Print the file list.
    print_files(file_list)


# --------------------
# PROGRAM CODE
# --------------------

if __name__ == "__main__":
    main()
