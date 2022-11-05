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
import typing

# --------------------
# TYPES
# --------------------


# --------------------
# DATA TYPES
# --------------------
DatasetIndex = int
FilePath = str
FileHash = typing.Union[str, None]
FileSize = typing.Union[int, None]
FileMenuId = typing.Union[int, None]


class FileData(object):
    __slots__ = ("size", "path", "md5_hash", "file_menu_id")

    def __init__(self, file_path: str):
        self.path: FilePath = file_path
        self.size: FileSize = os.path.getsize(file_path)
        self.md5_hash: FileHash = None
        self.file_menu_id: FileMenuId = None

    def calculate_md5_hash(self):
        hash_generator = hashlib.md5()
        with open(self.path, 'br') as f:
            hash_generator.update(f.read())
        self.md5_hash = hash_generator.hexdigest()


FilesDataset = typing.Dict[DatasetIndex, FileData]
DatasetIndexList = typing.List[DatasetIndex]
ByHashView = typing.Dict[FileHash, DatasetIndexList]
BySizeView = typing.Dict[FileSize, ByHashView]
FileMenuIds = typing.Dict[FileMenuId, DatasetIndex]

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


def build_files_dataset(
        root_dir: FilePath, file_extension: str) -> FilesDataset:
    """ Create a dataset of files of a given format in a given root dir.

    The files are recursively searched in the entire tree starting
    from the root_dir.
    :param root_dir: A string representing the path to the root
                        directory which is to be recursively scanned.
    :param file_extension: The extension by which the files are
                            to be filtered
    :return: A dictionary of the format {entry_id: file_entry_dict}.
    """
    files_dataset: FilesDataset = {}
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(file_extension):
                files_dataset[len(files_dataset)] = (
                    FileData(os.path.join(root, file)))
    return files_dataset


def create_size_hash_view(
        files_dataset: FilesDataset, sort_order: str) -> BySizeView:
    unsorted_view = {}
    for dataset_index, file_data in files_dataset.items():
        file_size = file_data.size
        file_hash = file_data.md5_hash
        if file_size not in unsorted_view:
            unsorted_view[file_size] = {file_hash: [dataset_index]}
        else:
            if file_hash not in unsorted_view[file_size]:
                unsorted_view[file_size][file_hash] = [dataset_index]
            else:
                unsorted_view[file_size][file_hash].append(dataset_index)
    if sort_order == SORT_CHOICE_ASCENDING:
        sorted_view = {
            file_size: unsorted_view[file_size]
            for file_size
            in sorted(unsorted_view.keys())}
    else:
        sorted_view = {
            file_size: unsorted_view[file_size]
            for file_size
            in sorted(unsorted_view.keys(), reverse=True)}
    return sorted_view


def filter_file_dataset(
        files_dataset: FilesDataset, by_view_filter: BySizeView):
    deleted_sizes = []
    for file_size, by_hash_view in by_view_filter.items():
        delete_hushes = []
        for file_hash, dataset_indexes in by_hash_view.items():
            if len(dataset_indexes) == 1:
                del files_dataset[dataset_indexes[0]]
                delete_hushes.append(file_hash)
        for file_hash in delete_hushes:
            del by_hash_view[file_hash]
        if len(by_hash_view) == 0:
            deleted_sizes.append(file_size)
    for file_size in deleted_sizes:
        del by_view_filter[file_size]


def update_file_menu_ids(
        file_menu_ids: FileMenuIds, by_size_view: BySizeView,
        files_dataset: FilesDataset):
    file_menu_ids.clear()
    menu_id: FileMenuId = 1
    for by_hash_view in by_size_view.values():
        for dataset_indexes in by_hash_view.values():
            for dataset_index in dataset_indexes:
                files_dataset[dataset_index].file_menu_id = menu_id
                file_menu_ids[menu_id] = dataset_index
                menu_id += 1


def print_file_menu(
        size_hash_view: BySizeView, files_dataset: FilesDataset,
        print_hashes: bool = False, print_menu_ids: bool = False):
    for size, by_hash_view in size_hash_view.items():
        print(MSG_FILE_SIZE_BYTES.format(SIZE=size))
        for file_hash, dataset_index_list in by_hash_view.items():
            if print_hashes:
                print(MSG_FILE_HASH_HEX_DIGEST.format(HASH=file_hash))
            for dataset_index in dataset_index_list:
                file_data = files_dataset[dataset_index]
                if print_menu_ids:
                    print(MSG_FILE_CHOICE.format(
                        FILE_ID=file_data.file_menu_id,
                        FILE_PATH=file_data.path))
                else:
                    print(file_data.path)


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


def calculate_md5_file_hashes(files_dataset: FilesDataset):
    for file_data in files_dataset.values():
        file_data.calculate_md5_hash()


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
    # and create an initial dataset of files of the matching format.
    files_dataset = build_files_dataset(root_dir, file_format)

    # Create a view of the data set grouping files by their sizes.
    # To avoid creating nearly identical functions a single function
    # is used both here and later for the size->hash grouping,
    # this works because at this point all files have None as their
    # hash and thus fall into a single hash group.
    size_hash_view = create_size_hash_view(files_dataset, sort_order)

    # Use the size_hash_view to filter the files data set
    # for same sized files.
    filter_file_dataset(files_dataset, by_view_filter=size_hash_view)

    # Print the filtered (by size only) dataset.
    # Again to avoid creating nearly identical functions a single
    # function is used both here and later for the size->hash menu,
    print_file_menu(size_hash_view, files_dataset)

    # Query user if they want to check for duplicates.
    check_duplicates = query_check_duplicates()

    # Terminate program if duplicates check is not needed.
    if not check_duplicates:
        return

    # Calculate hashes for all files in the dataset.
    calculate_md5_file_hashes(files_dataset)

    # Re-create the size_hash_view to account
    # for the newly calculated hashes.
    size_hash_view = create_size_hash_view(files_dataset, sort_order)

    # Re-filter the dataset for duplicates (files that have both
    # the same size and the same hash).
    filter_file_dataset(files_dataset, by_view_filter=size_hash_view)

    # Create and Update the file menu identifiers (as they
    # are None at this point).
    file_menu_ids = {}
    update_file_menu_ids(file_menu_ids, size_hash_view, files_dataset)

    # Print the filtered (by size and hashes) dataset with
    # file menu identifiers.
    print_file_menu(
        size_hash_view, files_dataset,
        print_hashes=True, print_menu_ids=True)


# --------------------
# PROGRAM CODE
# --------------------

if __name__ == "__main__":
    main()
