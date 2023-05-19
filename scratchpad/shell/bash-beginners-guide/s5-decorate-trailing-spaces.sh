#!/usr/bin/env bash

# s5-decorate-trailing-spaces.sh
# 7.  Create a script that shows lines containing trailing white spaces from a file. This script should use a sed script and show sensible information to the user.

TEST_FILE=./s5-trailing-spaces-demo.txt

sed --silent --file=s5-decorate-trailing-spaces.sed $TEST_FILE
