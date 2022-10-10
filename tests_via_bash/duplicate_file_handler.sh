#!/usr/bin/env bash

# duplicate_file_handler.sh
#

source ./_shared_functions.sh

TEST_SCRIPT_PREFIX="$PROJECTS_ROOT""duplicate_file_handler/stage_"

function test_stage_01() {
    TEST_SCRIPT_PATH="$TEST_SCRIPT_PREFIX""1.py"
    print_test_info
    test_via_args /dev/shm/test
    test_via_args
}

function test_stage_02() {
    TEST_SCRIPT_PATH="$TEST_SCRIPT_PREFIX""2.py"
    print_test_info
    test_via_args /dev/shm/test
    test_via_args
}

function test_stage_03() {
    TEST_SCRIPT_PATH="$TEST_SCRIPT_PREFIX""3.py"
    print_test_info
    test_via_args
    test_via_stdin
}

function test_stage_04() {
    TEST_SCRIPT_PATH="$TEST_SCRIPT_PREFIX""4.py"
    print_test_info
    test_via_args
}

#test_stage_01
test_stage_02
#test_stage_03
#test_stage_04
