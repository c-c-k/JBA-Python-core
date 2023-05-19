#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""DUPLICATE FILE HANDLER - stage 2: How much does it weigh?

Finds and handles duplicate files in the tree of a given root dir.
Stage 2 assignment requirements:
    - Read from system arguments the path to the root directory which is
      to be checked for duplicate files.
    - Ask the user for the file format (extension) of the files they wish
      to check for duplicates. An empty string will indicate that the user
      wishes to check all files.
    - Recursively scan the given root dir and it's subdirectories for files
      with the same size.
    - Ask the user if they want to sort the files of the same size in ascending
      or descending order.
    - For each group of same sized files, print their size and absolute
      paths in the order chosen by the user.
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
SORT_DESCENDING = 1
SORT_ASCENDING = 2
VALID_ORDER = (None, "1", "2")  # The None is added to align the indexes with the constants.

# --------------------
# MESSAGES
# --------------------

MSG_FILE_FORMAT = "Enter file format:"
MSG_SORT_CHOICE = "Enter a sorting option:"
MSG_ERR_DIR_MISSING = "Directory is not specified"
MSG_ERR_WRONG_OPTION = "Wrong option"
MSG_ASK_SORT_ORDER = (
    "Size sorting options:\n"
    "1. Descending\n"
    "2. Ascending")
MSG_FILE_SIZE_BYTES = "{SIZE} bytes"


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


def get_filtered_files(root_dir: str, extension: str) -> dict:
    """ Create a dictionary of filtered files grouped by size.

    :param root_dir: A string representing the root path to the directory
                     which is to be recursively scanned.
    :param extension: The extension by which the files are to be filtered
    :return: A dictionary of the format {filesize: [filepath, ..]}.
    """
    filtered_files = {}
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(extension):
                filepath = os.path.join(root, file)
                filesize = os.path.getsize(filepath)
                if filesize in filtered_files:
                    filtered_files[filesize].append(filepath)
                else:
                    filtered_files[filesize] = [filepath]
    return filtered_files


def filter_duplicates(files: dict) -> dict:
    """ Filter a dictionary containing files grouped by size for duplicate files.

    Duplicate files are those that have the same size.
    :param files: A dictionary containing lists of file paths grouped by size.
    :return: A filtered dictionary containing only those items that
             have a filelist longer than 1.
    """
    return {size: filelist for (size, filelist) in files.items() if len(filelist) > 1}


def print_duplicates(duplicates: dict, sort_order: int):
    """ Print the duplicates sorted and grouped by size.

    :param duplicates: A dictionary containing the duplicate files grouped by size.
    :param sort_order: An int representing the sort order.
    :return: None.
    """
    sorted_by_size = sorted(duplicates.items())
    if sort_order == SORT_DESCENDING:
        sorted_by_size.reverse()
    for entry in sorted_by_size:
        print(MSG_FILE_SIZE_BYTES.format(SIZE=entry[0]))
        for filepath in entry[1]:
            print(filepath)


def get_file_format() -> str:
    """ Get the format of the files that are to be checked.

    Ask the user for the file format (extension) which
    they wish to check for duplicates.
    An Empty input is acceptable and means that all files are to be checked.
    :return: A string representing the format of the files to be checked.
    """
    print(MSG_FILE_FORMAT)
    return input()


def get_sort_order() -> int:
    """ Get the sort order in which the duplicate files are to be printed

    Repeatedly ask the user for order in which they wish to see
    the duplicate files until they provide a valid input.
    A valid input is considered one of the strings in the VALID_ORDER constant.
    :return: An integer representing the order in which the files are to be sorted.
    """
    print(MSG_ASK_SORT_ORDER)
    while True:
        print(MSG_SORT_CHOICE)
        sort_order = input()
        if sort_order == VALID_ORDER[SORT_ASCENDING]:
            return SORT_ASCENDING
        elif sort_order == VALID_ORDER[SORT_DESCENDING]:
            return SORT_DESCENDING
        else:
            print(MSG_ERR_WRONG_OPTION)


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

    # Get missing parameters (file format filter and sort direction)
    # from standard input.
    file_format = get_file_format()
    sort_order = get_sort_order()

    # Walk the directory tree starting from the given root dir and record all
    # files of the matching format into a dictionary keyed by file size.
    filtered_files = get_filtered_files(root_dir, file_format)

    # Filter the dictionary for duplicates (entries containing more than a
    # single file per file size).
    duplicate_files = filter_duplicates(filtered_files)

    # Print the entries from the filtered dictionary.
    print_duplicates(duplicate_files, sort_order)

    pass


# --------------------
# PROGRAM CODE
# --------------------

if __name__ == "__main__":
    main()
