#!/usr/bin/env bash

set -x

# s6-awk-examples.sh
# This is a copy of the examples presented in chapter 6.

#----------------------------------------------------------
# 6.2.1 - printing selected fields
#----------------------------------------------------------
# -- prepare example data
TEST_DIR=/dev/shm/demodir621
mkdir $TEST_DIR
cp -t $TEST_DIR $(ls | sed -n -e'3,8p')
# --
ls -l $TEST_DIR | awk '{ print $5 $9 }'
ls -l $TEST_DIR | awk '{ print $5, $9 }'
# -- clean example data --
rm -fr $TEST_DIR
unset -v TEST_DIR
# --
echo $'\n\n'


#----------------------------------------------------------
# 6.2.2 - formating fields
#----------------------------------------------------------
# -- prepare example data
TEST_DIR=/dev/shm/demodir621
mkdir $TEST_DIR
cp -t $TEST_DIR $(ls | sed -n -e'3,8p')
# --
ls -ldh $TEST_DIR/* | grep -v 'total' | sed -e's:/.*/::'| \
    awk '{ print "Size is " $5 "b for " $9}'
df -h | sort -rnk 5 | head -3 | \
    awk '{ print "Partition " $6 " \t: " $5 " full!"}'
# -- clean example data --
rm -fr $TEST_DIR
unset -v TEST_DIR
# --
echo $'\n\n'


#----------------------------------------------------------
# 6.2.3 - The print command and regular expressions
#----------------------------------------------------------
df -h | awk '/dev\/sd/{ print $6 " \t: " $5}'
ls -l /etc | awk '/\<(a|x).*\.conf$/ { print $9 }'
echo $'\n\n'


#----------------------------------------------------------
# 6.2.4 - Special patterns
#----------------------------------------------------------
ls -l /etc | \
    awk 'BEGIN { print "---\tList of \".conf\" Files found in \"/etc\"\n\tthat start with the characters \"a\" or \"x\" :" } /\<[ax].*\.conf$/ {print $9} END { print "---\tEnd of file list.\n" }'
echo $'\n\n'


#----------------------------------------------------------
# 6.2.5 Scripts
#----------------------------------------------------------
df -h | awk -f ./6-diskrep.awk
echo $'\n\n'


#----------------------------------------------------------
# 6.3.1 - Gawk variables
#----------------------------------------------------------
awk 'BEGIN { FS=":" } /bash/ { print $1 "\t" $5 }' /etc/passwd
awk -f ./6-printnames.awk /etc/passwd
# important note: remember to consider that the Field Separator might have
# unexpected usage in the input data.
echo $'\n\n'


#----------------------------------------------------------
# 6.3.2 - The output separators
#----------------------------------------------------------
# -- prepare example data
echo $'record1\t\tdata1\nrecord2\t\tdata2' > /dev/shm/test-632.tmp
cat /dev/shm/test-632.tmp
# --
awk '{ print $1 $2}' /dev/shm/test-632.tmp
awk '{ print $1, $2}' /dev/shm/test-632.tmp
awk 'BEGIN { OFS=";" ; ORS="\n-->\n" } { print $1, $2}' /dev/shm/test-632.tmp
awk 'BEGIN { OFS=";" ; ORS="-->" } { print $1, $2}' /dev/shm/test-632.tmp
# -- clean example data
rm /dev/shm/test-632.tmp
# --
echo $'\n\n'


#----------------------------------------------------------
# 6.3.3 - The number of records
#----------------------------------------------------------
# -- prepare example data
echo $'record0\t\tdata1\nrecord2\t\tdata2' > /dev/shm/test-633.tmp
cat /dev/shm/test-633.tmp
# --
awk -f ./5-processed.awk /dev/shm/test-633.tmp
# -- clean example data
rm /dev/shm/test-633.tmp
# --
echo $'\n\n'


#----------------------------------------------------------
# 6.3.4 - User defined variables
#----------------------------------------------------------
# -- prepare example data
echo $'20021009\t20021013\tconsultancy\tBigComp\t2500\n' \
    $'20021015\t20021020\ttraining\tEduComp\t2000\n' \
    $'20021112\t20021123\tappdev\tSmartComp\t10000\n' \
    $'20021204\t20021215\ttraining\tEduComp\t5000' \
    > /dev/shm/test-634.tmp
cat /dev/shm/test-634.tmp
awk -f ./6-total.awk /dev/shm/test-634.tmp
# -- clean example data
rm /dev/shm/test-634.tmp
# --
echo $'\n\n'


#----------------------------------------------------------
# 6.3.5 - More examples
#----------------------------------------------------------
# -- prepare example data
TEST_FILE_INPUT=/dev/shm/test-635.txt
TEST_FILE_OUTPUT=/dev/shm/test-635.html
echo $'Line 1\nLine 2\nLine 3' > $TEST_FILE_INPUT
cat $TEST_FILE_INPUT
# --
awk -f ./6-make-html-from-text.awk $TEST_FILE_INPUT > $TEST_FILE_OUTPUT
cat $TEST_FILE_OUTPUT
# -- clean example data
rm $TEST_FILE_INPUT
rm $TEST_FILE_OUTPUT
unset -v ${!TEST_FILE*}
# --
echo 'awk examples in startup files in "/etc/init.d" :'
grep awk /etc/init.d/*
echo $'\n\n'


#----------------------------------------------------------
# 6.3.6 - The printf option
#----------------------------------------------------------
# see awk info pages


