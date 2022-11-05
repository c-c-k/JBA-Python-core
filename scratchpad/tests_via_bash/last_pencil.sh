#!/usr/bin/env bash

# template_test.sh
#

source ./_shared_functions.sh
TEST_SCRIPT_PREFIX="$PROJECTS_ROOT""last_pencil/stage_"

function test_stage_01() {
    TEST_SCRIPT_PATH="$TEST_SCRIPT_PREFIX""1.py"
    print_test_info
    test_via_stdin
}

function test_stage_02() {
    TEST_SCRIPT_PATH="$TEST_SCRIPT_PREFIX""2.py"
    print_test_info
    test_via_stdin 5 player1
    test_via_stdin 20 player2
}

function test_stage_03() {
    TEST_SCRIPT_PATH="$TEST_SCRIPT_PREFIX""3.py"
    print_test_info
    test_via_stdin 5 Player1 2 1 2
    test_via_stdin 15 Player1 8 7
}

function test_stage_04() {
    TEST_SCRIPT_PATH="$TEST_SCRIPT_PREFIX""4.py"
    print_test_info
    test_via_stdin a 5
    test_via_stdin 0 20
    test_via_stdin 5 illegalname Player1
    test_via_stdin 5 Player1 4 1
    test_via_stdin 5 Player1 a 1
    test_via_stdin 5 Player1 3 3 2
}

function test_stage_05() {
    TEST_SCRIPT_PATH="$TEST_SCRIPT_PREFIX""5.py"
    print_test_info
    test_via_stdin 10 Bot 2 1 1
    test_via_stdin 6 Player 1 2
}

#test_stage_01
#test_stage_02
#test_stage_03
#test_stage_04
test_stage_05
