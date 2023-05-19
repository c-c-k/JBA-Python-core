#!/usr/bin/env -S bash -o xtrace

# special_variables.sh
# This script demonstrates the special variables $$, $!, $?, $0, $_

SCRIPT_PATH=$_
clear
echo "The path to this script is $SCRIPT_PATH"
grep dictionary /usr/share/dict/words
echo "The last argument to the previous command was: $_"
echo "The id of the current shell is: $$"
mozzila &
echo "The id of the last process that was run in this shell is: $!"
ls doesnotexist
echo "The exit status of the last pipeline was: $?"
echo "The name of this script is: $0"
echo "The exit status of the last pipeline was: $?"
