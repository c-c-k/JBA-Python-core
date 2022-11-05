#!/usr/bin/env bash

# c26-SORTING_AND_DEDUPLICATION.sh
#

# Display all the duplicates from the /tmp/test.txt file. Please, do not
# forget to sort the lines first!
function display_the_duplicates() {
  # create test file
  echo -ne "stream\ndata\ncomputer\nstream\n" > "/tmp/test.txt"
  # script
  sort "/tmp/test.txt" | uniq -D
  # cleanup test file
  rm "/tmp/test.txt"
}

# Use the sort command to print the lines from the /tmp/test.txt file in
# lexicographic order.
function sort_the_data() {
  # create test file
  echo -ne "laptop\nnotebook\nscreen\ninternet\n" > "/tmp/test.txt"
  # script
  sort "/tmptest.txt"
  # cleanup test file
  rm "/tmp/test.txt"
}
