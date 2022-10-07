#!/usr/bin/env bash

# shared_functions.sh
#

PROJECTS_ROOT="../"

function test_via_stdin() {
  echo "-- TEST START --"
  echo -e "\033[01mTEST INPUTS: ""$*\033[00m"
  TEST_INPUTS="$1"
  shift
  for TEST_INPUT ;do TEST_INPUTS="$TEST_INPUTS""\n""$TEST_INPUT"; done
  echo -ne "$TEST_INPUTS"|python3 "$TEST_SCRIPT_PATH"
  echo -e "-- TEST END --\n"
}

function test_via_args() {
  echo "-- TEST START --"
  echo -e "\033[01mTEST INPUTS: ""$*\033[00m"
  python3 "$TEST_SCRIPT_PATH" "$@"
  echo -e "-- TEST END --\n"
}

function print_test_info() {
    echo -e "--- from \033[01m${0}\033[00m running tests for \033[01m${TEST_SCRIPT_PATH}\033[00m ---"
}
