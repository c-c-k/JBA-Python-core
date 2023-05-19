#!/usr/bin/env bash

set -x

# s6-ex3-xml-from-tab-list.sh
# This script is a solution for the third exercise of chapter 6.
# First it generates a test data file with the following input lines:
# 
## Meaning   very long line  with a lot of description
##  
## meaning another   long line
##  
## othermeaning    more longline
##  
## testmeaning     looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong line, but i mean really looooooooooooooooooooooooooooooooooooooooooooooooooong.
##  
# Then it runs it through the "s6-ex3-xml-from-tab-list.awk" awk script to generate the following output:
# 
# <row>
# <entry>Meaning</entry>
# <entry>
# very long line
# </entry>
# </row>
# <row>
# <entry>meaning</entry>
# <entry>
# long line
# </entry>
# </row>
# <row>
# <entryothermeaning</entry>
# <entry>
# more longline
# </entry>
# </row>
# <row>
# <entrytestmeaning</entry>
# <entry>
# looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong line, but i mean really looooooooooooooooooooooooooooooooooooooooooooooooooong.
# </entry>
# </row>
# 


# -- Set variables for script and data file paths --
DATA_FILE="/dev/shm/test-data-$$-$(date +%s).tmp"
SCRIPT_FILE=./s6-ex3-xml-from-tab-list.awk
# -- prepare test data --
echo -n $'Meaning\tvery long line\twith a lot of description\n'\
$'meaning another\tlong line\n'\
$'othermeaning\tmore longline\n'\
$'testmeaning\t'\
$'looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong '\
$'line, but i mean really'\
$'looooooooooooooooooooooooooooooooooooooooooooooooooong.\n'\
> $DATA_FILE
cat $DATA_FILE
# -- execute awk script
awk --file=$SCRIPT_FILE $DATA_FILE
# -- cleanup
rm --force $DATA_FILE
unset -v DATA_FILE SCRIPT_FILE

#
