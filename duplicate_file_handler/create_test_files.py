#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Summary

Description
"""


# --------------------
# IMPORTS
# --------------------
# Standard library modules:
import os
import random


# --------------------
# CONSTANTS
# --------------------
TEST_ROOT = "/dev/shm/"
FILE_UNIQUE_TEMPLATE = "unique_{}.tmp"
FILE_SAME_SIZE_TEMPLATE = "same_size_{}.tmp"
FILE_SAME_HASH_TEMPLATE = "same_hash_{}.tmp"
TEST_DIR_TEMPLATE = os.path.join(TEST_ROOT, "test_dir_{}")
RANDOM_SEED = 42
NUM_TEST_DIRS = 3
NUM_UNIQUE_FILES = 3
NUM_SAME_SIZE_FILES = 3
NUM_SAME_HASH_FILES = 3

# --------------------
# FUNCTIONS
# --------------------
def create_test_dirs():
    for num in range(NUM_TEST_DIRS):
        os.makedirs(TEST_DIR_TEMPLATE.format(num), exist_ok=True)

def create_unique_files():
    for num in range(NUM_UNIQUE_FILES):


def main():
    test_dir_1 = os.path.join(test_root, "dir_1")
    test_dir_2 = os.path.join(test_root, "dir_2")
    unique_dir_2 = os.path.join(test_dir_2, "unique")
    same_size_dir_2 = os.path.join(test_dir_2, "same_size")
    same_hash_dir_2 = os.path.join(test_dir_2, "same_hash")
    pass


# --------------------
# PROGRAM CODE
# --------------------

if __name__ == "__main__":
    main()
