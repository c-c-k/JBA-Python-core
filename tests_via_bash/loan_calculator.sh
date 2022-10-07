#!/usr/bin/env bash

# template_test.sh
#

source ./_shared_functions.sh

function test_stage_01() {
  TEST_SCRIPT_PATH="$PROJECTS_ROOT""loan_calculator/stage_1.py"
  print_test_info
  test_via_stdin
}

function test_stage_02() {
  TEST_SCRIPT_PATH="$PROJECTS_ROOT""loan_calculator/stage_2.py"
  print_test_info
  test_via_stdin 1000 m 150
  test_via_stdin 1000 m 1000
  test_via_stdin 1000 p 10
  test_via_stdin 1000 p 9
}

function test_stage_03() {
  TEST_SCRIPT_PATH="$PROJECTS_ROOT""loan_calculator/stage_3.py"
  print_test_info
  test_via_stdin n 1000000 15000 10
  test_via_stdin a 1000000 60 10
  test_via_stdin p 8721.8 120 5.6
}

test_stage_01
test_stage_02
test_stage_03
