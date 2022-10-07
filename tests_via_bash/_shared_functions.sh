#!/usr/bin/env bash

# shared_functions.sh
#

PROJECTS_ROOT="../"

function test_via_stdin() {
  echo "TEST INPUTS: ""$*"
  TEST_INPUTS="$1"
  shift
  for TEST_INPUT ;do TEST_INPUTS="$TEST_INPUTS""\n""$TEST_INPUT"; done
  echo -ne "$TEST_INPUTS"|python3 "$TEST_SCRIPT_PATH"
}

function test_via_args() {
  echo "TEST INPUTS: ""$*"
  python3 "$TEST_SCRIPT_PATH" "$@"
}

function print_test_info() {
    echo -e "--- from \033[01m${0}\033[00m running tests for \033[01m${TEST_SCRIPT_PATH}\033[00m ---"
}
