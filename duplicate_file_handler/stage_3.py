#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""DUPLICATE FILE HANDLER - stage 3: What's that hash about?

Finds and handles duplicate files in the tree of a given root dir.
Stage 3 assignment requirements:
    - Carry over stage 2 requirements:
        - Read from system arguments the path to the root directory
            which is to be checked for duplicate files.
        - Ask the user for the file format (extension) of the files
            they wish to check for files.
            - An empty string will indicate that the user wishes to
                check all files.
        - Recursively scan the given root dir and it's subdirectories
            for same sized files of the specified format and group
            them by their sizes.
        - Ask the user if they want to sort the same sized files
            in ascending or descending order.
            - Only accept the answers "1" or "2", keep asking until
                a valid answer is given.
        - Print each group of same sized files in the sort order that
            the user chose, the format should be:
                {SIZE IN BYTES} bytes
                {FILE PATH}
                {FILE PATH}
                ...
    - Ask the user if they want to check the same sized files
        for files.
        - Only accept the answers "yes" or "no", keep asking until
            a valid answer is given.
        - In case the user answers 'no' terminate the program.
    - Generate and store a md5 hash for each of the same sized files.
    - Sub-group each group of same sized files by their hashes.
        - (The data structure is file size -> file hash -> file path).
    - Attach to each file path a sequential integer identifier (1,2..).
        - The identifiers are meant to let the user choose the files
            they wish to delete in the next stage.
    - Print each group of same sized files in the sort order that
        the user chose, subgroup by the files hashes (order of
        the subgroups doesn't matter), the format should be:
            {SIZE IN BYTES} bytes
            Hash: {SUBGROUP HASH}
            {FILE ID}. {FILE PATH}
            {FILE ID}. {FILE PATH}
            Hash: {SUBGROUP HASH}
            {FILE ID}. {FILE PATH}
            {FILE ID}. {FILE PATH}
            ...
"""

# --------------------
# IMPORTS
# --------------------
# Standard library modules:
import argparse
import hashlib
import os


# --------------------
# CONSTANTS
# --------------------
# SORT CHOICE constants must coincide with MSG_SORT_MENU.
SORT_CHOICE_DESCENDING = "1"
SORT_CHOICE_ASCENDING = "2"
VALID_SORT_CHOICES = (SORT_CHOICE_ASCENDING, SORT_CHOICE_DESCENDING)
CHOICE_YES = "yes"
CHOICE_NO = "no"
VALID_CHECK_DUPLICATES_CHOICES = (CHOICE_YES, CHOICE_NO)

# --------------------
# MESSAGES
# --------------------

MSG_ASK_FORMAT = "Enter file format:"
MSG_ASK_SORT_CHOICE = "Enter a sorting option:"
MSG_ASK_CHECK_DUPLICATES = "Check for files?"
MSG_ERR_DIR_MISSING = "Directory is not specified"
MSG_ERR_WRONG_OPTION = "Wrong option"
MSG_FILE_HASH_HEX_DIGEST = "Hash: {HASH}"
MSG_FILE_SIZE_BYTES = "{SIZE} bytes"
MSG_FILE_CHOICE = "{FILE_ID}. {FILE_PATH}"
# MSG_SORT_MENU must coincide with SORT_CHOICE constants.
MSG_SORT_MENU = (
    "Size sorting options:\n"
    "1. Descending\n"
    "2. Ascending")


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


def filter_same_size(files_dict: dict):
    """ Filter the files dictionary for same sized files.

    :param files_dict: A dictionary containing lists of file paths
                        grouped by size.
    :return: A filtered dictionary containing only those items that
             have a filelist longer than 1.
    """
    for file_size, file_list in files_dict.items():
        if len(file_list) == 1:
            files_dict.pop(file_size)


def print_files_by_size(files: dict, sort_order: str):
    """ Print the same sized files grouped by size.

    :param files: A dictionary containing same sized files
                    grouped by size.
    :param sort_order: A string representing the sort order.
    :return: None.
    """
    sorted_by_size = sorted(files.items())
    if sort_order == SORT_CHOICE_DESCENDING:
        sorted_by_size.reverse()
    for size, file_paths in sorted_by_size:
        print(MSG_FILE_SIZE_BYTES.format(SIZE=size))
        for filepath in file_paths:
            print(filepath)


def query_file_format() -> str:
    """ Get the format of the files that are to be checked.

    Ask the user for the file format (extension) of the files
        they wish to check.
    An Empty input is acceptable and means that all files
        are to be checked.
    :return: A string representing the format of the files to be checked.
    """
    print(MSG_ASK_FORMAT)
    return input()


def query_sort_order() -> str:
    """ Get the sort order in which the results are to be printed.

    Repeatedly ask the user for order in which they wish to see
    the duplicate files until they provide a valid input.
    A valid input is considered to be one of the strings in the
        VALID_ORDER constant.
    :return: A string representing the order in which the files are
                to be sorted.
    """
    print(MSG_SORT_MENU)
    while True:
        print(MSG_ASK_SORT_CHOICE)
        sort_order = input()
        if sort_order in VALID_SORT_CHOICES:
            return sort_order
        else:
            print(MSG_ERR_WRONG_OPTION)


def query_check_duplicates() -> bool:
    """ Query the user if they wish to check for duplicates.

    Repeatedly ask the user if they want to check the list of
        same sized files to be checked for duplicates until the
        user gives a valid reply.
        A valid reply is one of the values
    :return: True if the reply is "yes", false if the reply is "no".
    """
    while True:
        print(MSG_ASK_CHECK_DUPLICATES)
        choice = input()
        if choice == CHOICE_YES:
            return True
        elif choice == CHOICE_NO:
            return False


def generate_md5_file_hash(file_path: str) -> str:
    hash_generator = hashlib.md5()
    with open(file_path, 'br') as f:
        hash_generator.update(f.read())
    return hash_generator.hexdigest()


def add_to_hashes_dict(hashes_dict: dict, file_path: str):
    """ Add a file path to a hash subgroup.

    :param hashes_dict: A dictionary grouping files by their hashes.
    :param file_path: The path of the file to be added into a hash group.
    """
    file_hash = generate_md5_file_hash(file_path)
    if file_hash in hashes_dict:
        hashes_dict[file_hash].append(file_path)
    else:
        hashes_dict[file_hash] = [file_path]


def subgroup_by_hashes(files_dict: dict):
    """ Regroup and subgroup by hashes.

    For each file size entry in files_dict, replace the file paths list
    with a dictionary grouping the files by their hashes.
    :param files_dict: A dictionary of files grouped by size.
    """
    for file_size, file_paths in files_dict.items():
        hashes_dict = {}
        for file_path in file_paths:
            add_to_hashes_dict(hashes_dict, file_path)
        files_dict[file_size] = hashes_dict


def prune_non_duplicates(files_dict: dict):
    """ Remove size and hash entries that only have one file per hash.

    :param files_dict: A dictionary of files grouped by size and
                        subgrouped by their hashes.
    """
    for size, hashes_dict in files_dict.items():
        for file_hash, file_paths in hashes_dict.items:
            if len(file_paths) == 1:
                hashes_dict.pop(file_hash)
        if len(hashes_dict) == 0:
            files_dict.pop(size)


def filter_duplicates(files_dict: dict):
    """ Filter and subgroup files_dict by duplicates.

    Duplicates are determined by same sized files that also
        have the same hash.
    :param files_dict: A dictionary of files grouped by size.
    """
    subgroup_by_hashes(files_dict)
    prune_non_duplicates(files_dict)


def print_duplicates(files_dict: dict):
    """ Print the duplicate files.

    The output should be grouped by sizes and hashes and include
    per file path id's that will be used in the next stage.
    :param files_dict: A dictionary of files grouped by size and
                        subgrouped by their hashes.
    """
    pass


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

    # Query user for missing parameters (file format filter
    # and sort direction)a.
    file_format = query_file_format()
    sort_order = query_sort_order()

    # Walk the directory tree starting from the given root dir
    # and record all files of the matching format into a dictionary
    # keyed by file size.
    files_dict = get_filtered_files(root_dir, file_format)

    # Filter the dictionary for same sized files (entries containing
    # more than a single file per file size).
    filter_same_size(files_dict)

    # Print the entries from the filtered dictionary.
    print_files_by_size(files_dict, sort_order)

    # Query user if they want to check for duplicates.
    check_duplicates = query_check_duplicates()

    # Terminate program if duplicates check is not needed.
    if not check_duplicates:
        return

    # Filter and subgroup the files dictionary by duplicates.
    filter_duplicates(files_dict)

    # Print the duplicates.
    print_duplicates(files_dict)


# --------------------
# PROGRAM CODE
# --------------------

if __name__ == "__main__":
    main()
