#!/usr/bin/env bash

# template_test.sh
#

source ./_shared_functions.sh
TEST_SCRIPT_PREFIX="$PROJECTS_ROOT""/last_pencil/stage_"

function test_stage_01() {
    TEST_SCRIPT_PATH="$TEST_SCRIPT_PREFIX""1.py"
    print_test_info
    test_via_stdin
}

function test_stage_02() {
    TEST_SCRIPT_PATH="$TEST_SCRIPT_PREFIX""2.py"
    print_test_info
    test_via_args
    test_via_stdin
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
    test_via_stdin
}

function test_stage_05() {
    TEST_SCRIPT_PATH="$TEST_SCRIPT_PREFIX""5.py"
    print_test_info
    test_via_args
    test_via_stdin
}

test_stage_01
#test_stage_02
#test_stage_03
#test_stage_04
#test_stage_05
