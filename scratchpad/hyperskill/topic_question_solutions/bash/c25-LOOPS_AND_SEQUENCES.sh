#!/usr/bin/env bash

# c25-LOOPS_AND_SEQUENCES.sh
#

function simple_loop_output() {
    for i in $(seq "$1" "$2")
    do
      echo "Number: $i"
    done
}

# Two sequences
# Run the conditional for loop with the input range from 1 to 10 and set a
# condition to skip the values from 3 to 7
function two_sequences() {
    for i in $(seq "$1" "$2")
    do
      if [ "$i" -lt "3" ] || [ "$i" -gt "7" ] ; then
        echo "$i"
      fi
    done
}