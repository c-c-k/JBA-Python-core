#!/usr/bin/env bash

# s5-x_sed-examples.sh
# Chapter 5 examples:

# 5.2.1 - printing lines containing a pattern

EXAMPLE1="./s5-2-x_example.txt"
echo 'cat $EXAMPLE1'
cat $EXAMPLE1
echo '------------' $'\n'

echo 'sed "/erors/p" $EXAMPLE1'
sed '/erors/p' $EXAMPLE1
echo '------------' $'\n'

echo 'sed -n "/erors/p" $EXAMPLE1'
sed -n "/erors/p" $EXAMPLE1
echo '------------' $'\n'


# 5.2.2 Deleting lines of input containing a pattern

echo 'sed "/erors/d" $EXAMPLE1'
sed "/erors/d" $EXAMPLE1
echo '------------' $'\n'

echo 'sed -n "/^This.*errors.*$/p" $EXAMPLE1'
sed -n "/^This.*errors.*$/p" $EXAMPLE1
echo '------------' $'\n'


# 5.2.3 - Ranges of lines

echo 'sed "3,\$d" $EXAMPLE1'
sed "3,\$d" $EXAMPLE1
echo '------------' $'\n'


echo 'sed -n "/a text/,/a line/p" $EXAMPLE1'
sed -n "/a text/,/a line/p" $EXAMPLE1
echo '------------' $'\n'

# 5.2.4 - Find and replace with sed

echo 'sed "s/erors/errors/" $EXAMPLE1'
sed "s/erors/errors/" $EXAMPLE1
echo '------------' $'\n'


echo 'sed "s/erors/errors/g" $EXAMPLE1'
sed "s/erors/errors/g" $EXAMPLE1
echo '------------' $'\n'

echo 'sed "s/^/> /" $EXAMPLE1'
sed "s/^/> /" $EXAMPLE1
echo '------------' $'\n'

echo 'sed "s/$/EOL/" $EXAMPLE1'
sed "s/$/EOL/" $EXAMPLE1
echo '------------' $'\n'


echo 'sed -e "s/erors/errors/g" -e "s/last/final/g"' $EXAMPLE1
sed -e "s/erors/errors/g" -e "s/last/final/g" $EXAMPLE1
echo '------------' $'\n'

echo 'cat ./s5-3-2_script.sed'
cat ./s5-3-2_script.sed
echo '------------' $'\n'

echo 'cat ./s5-3_txt2html.sh'
cat ./s5-3_txt2html.sh
echo '------------' $'\n'

echo $'line 1\nline 2\nline 3' > s5-3-2_test.txt
echo 'cat ./s5-3-2_test.txt'
cat ./s5-3-2_test.txt
echo '------------' $'\n'

echo './s5-3_txt2html.sh ./s5-3-2_test.txt'
./s5-3_txt2html.sh ./s5-3-2_test.txt
echo '------------' $'\n'

echo 'cat ./s5-3-2_test.txt'
cat ./s5-3-2_test.txt
echo '------------' $'\n'


