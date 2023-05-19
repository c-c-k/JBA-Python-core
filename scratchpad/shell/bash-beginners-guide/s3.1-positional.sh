#!/usr/bin/env bash

# positional.sh
# This script reads 3 positional parameters and prints them out.

clear

POSPARAM_1="$1"
POSPARAM_2="$2"
POSPARAM_3="$3"

echo "$POSPARAM_1 is the value of the first positional parameter, \$1"
echo "$POSPARAM_2 is the value of the second positional parameter, \$2"
echo "$POSPARAM_3 is the value of the third  positional parameter, \$3"
echo "There are a total of $# positional parameters"
echo "The positional parameters as output by \$* are: $*"
echo "The positional parameters as output by \$@ are: $@"
