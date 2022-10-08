#!/usr/bin/env bash

# template_test.sh
#

source ./_shared_functions.sh
TEST_SCRIPT_PREFIX="$PROJECTS_ROOT""$PROJECT_NAME/stage_"

function test_stage_01() {
  TEST_SCRIPT_PATH="$TEST_SCRIPT_PREFIX""1.py"
  print_test_info
  test_via_args
  test_via_stdin
}

test_stage_01
