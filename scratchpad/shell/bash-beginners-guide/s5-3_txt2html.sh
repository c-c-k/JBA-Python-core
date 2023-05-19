#!/usr/bin/env bash

# This is a simple script that you can use for converting text to HTML.
# First we take out all new line characters, so that the appending only happens
# once, then we replace the newlines.

echo "converting $1..."
SCRIPT="./s5-3-2_script.sed"
NAME="$1"
TEMPFILE="/dev/shm/sed.$PID.tmp"
sed "s/\n//" $1 | sed -f $SCRIPT | sed "s//\n/" > $TEMPFILE
mv $TEMPFILE $NAME

echo "done"
