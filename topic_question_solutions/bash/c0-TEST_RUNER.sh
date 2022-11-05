#!/usr/bin/env bash

# c0-TEST_RUNER.sh
#

#==================================================
# run_test definition
#==================================================
function run_test() {
  echo "-----"
  echo -n "-- Running test for function "
  echo -n "\"${TEST_FUNCTION_NAME:=$2}\""
  echo -n " in script file "
  echo -n "\"${TEST_FILE_NAME:=$1}\""
  echo " with the parameters :"
  shift 2
  echo "-- \"$*\""
  echo "-----"
  source "$TEST_FILE_NAME"
  "$TEST_FUNCTION_NAME" "$@"
  echo "-----"
  echo "-- TEST DONE"
  echo "-----"
}
#==================================================


#==================================================
# Tests
#==================================================

# Chapter 25 tests
#run_test "c25-LOOPS_AND_SEQUENCES.sh" "simple_loop_output" 1 5
#run_test "c25-LOOPS_AND_SEQUENCES.sh" "two_sequences" 1 10

# Chapter 26 tests
#run_test "c26-SORTING_AND_DEDUPLICATION.sh" "display_the_duplicates"
run_test "c26-SORTING_AND_DEDUPLICATION.sh" "sort_the_data"
