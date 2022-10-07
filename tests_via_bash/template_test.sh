#!/usr/bin/env bash

# template_test.sh
#

source ./_shared_functions.sh

function test_stage_0() {
  TEST_SCRIPT_PATH="$PROJECTS_ROOT""tests_via_bash/test_via_args.py"
  print_test_info
  test_via_args arg1 arg2
  TEST_SCRIPT_PATH="$PROJECTS_ROOT""tests_via_bash/test_via_input.py"
  print_test_info
  test_via_stdin line1 line2 line3
}

test_stage_0
