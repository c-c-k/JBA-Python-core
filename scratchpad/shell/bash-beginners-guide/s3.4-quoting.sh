#!/usr/bin/env bash

# s3.4-quoting.sh
# This script checks and demonstrated the different quoting rules.

set -o verbose  # Lazy way to print the remarks in the output.

# The backslash removes the  special meaning of characters.
SAMPLE_VAR=12345
echo $SAMPLE_VAR
echo \$SAMPLE_VAR
# An exception is if a newline character appears right after the backslash, in
# this it marks the continuation of a single line that is too wide to fit in
# the terminal.
# Demonstrating this in a script file is too difficult for me right now but
# pressing \<ENTER> in an interactive shell will cause the shell to switch to
# the $PS2 prompt and treat everything until the next <ENTER> as the
# continuation of the previous line.

# The single quote  (apostrophe) marks the beginning and the end of a raw
# string in which all special meanings are ignored. 
echo '$SAMPLE_VAR'
# A backslash cannot be used to escape a single quote between an outer pair of
# enclosing single quotes, the only way to insert a single quote in what is
# meant to be a raw string is to close the raw string before the single quote,
# insert a backslash escaped single quote (outside a raw string) and then
# start another raw string.
echo 'A backslash doesn'\''t have any special meaning inside apostrophes : \'

# Double quotes remove the special meaning of all characters except the backticks and the dollar sign.
echo ~ , "~" , "$SAMPLE_VAR" , "`date`"
# Within double quoted text a backslash can be used to escape a double quote,
# a backtick, a dollar sign and another backslash.
echo  "$SAMPLE_VAR" , "`date`" , "\$SAMPLE_VAR\" , \"\`date\`\\"

# ANSI-C quoting: single quoted text preceded by a dollar sign ($'...')
# replaces certain backslash escaped characters by their ANSI-C standard
# values. Usually the fastest way to find these replacement values is to
# search the bash man page for \<ANSI\>.
echo $'ab\bc n\n v\v t\t 64\64 64\x64 6644\u6644'

# Locales: double quoted strings preceded by a dollar sign ($"...") are
# translated according to local, this is an advanced and complex topic that
# can also introduce security risks, I might get to learning this someday...


