#!/usr/bin/env bash

# s4.1-grep-reports-demonstration.sh
# This script prints a series of reports generated mostly via grep.
# The reports generated are:
# 1 - Display a list of all the users on the system who log in with the Bash shell as a default.
# 2 - Display all lines starting with the string "daemon" from the /etc/group directory.
# 3 - Display all lines that do not contain the word "daemon" from the /etc/group directory.
# 4 - Count and Display with line numbers all lines containing localhost information from the /etc/hosts file.
# 5 - Display a list of /usr/share/doc subdirectories containing information about shells.
# 6 - Count the number of README files in the above mentioned subdirectories that have no file extension.
# 7 - Display a list of files in the home directory that were changed less that 10 hours ago, using grep, but leave out directories.

# NOTE: for increased clarity instead of using shell pipes, output is redirected to temporary input and output files in "/dev/shm".
#   After each command the temporary output file is renamed to be the temporary input file.
TEMP_IN="/dev/shm/GRT_TEMP_INPUT.TMP"
TEMP_OUT="/dev/shm/GRT_TEMP_OUTPUT.TMP"
shopt -s expand_aliases
alias switch_in_out='mv ${TEMP_OUT} ${TEMP_IN}'

#============================================================================
# 1 - Display a list of all the users on the system who log in with the Bash shell as a default.
#============================================================================

grep --regexp='bash$' -- /etc/passwd > ${TEMP_OUT}
switch_in_out
cut --delimiter=':' --fields='1' ${TEMP_IN} > ${TEMP_OUT}
switch_in_out
paste --delimiters=',' --serial ${TEMP_IN} > ${TEMP_OUT}
echo 'The users who login to this system with bash are:'
cat ${TEMP_OUT}
echo


#============================================================================
# 2 - Display all lines starting with the string "daemon" from the /etc/group directory.
#============================================================================

echo $'In the directory file "/etc/group" \n   the lines starting with the word daemon are:'
grep --regexp='^daemon' -- /etc/group
echo


#============================================================================
# 3 - Display all lines that do not contain the word "daemon" from the /etc/group directory.
#============================================================================

echo $'In the directory file "/etc/group" \n   the lines\033[01m not \033[00mstarting with the word daemon are:'
grep --invert-match --regexp='^daemon' -- /etc/group
echo


#============================================================================
# 4 - Count and Display with line numbers all lines containing localhost information from the /etc/hosts file.
#============================================================================

grep --line-number --initial-tab --fixed-strings \
    --regexp='localhost' -- /etc/hosts > ${TEMP_OUT}
NUM_INFO_LINES=$(grep --count --fixed-strings --regexp='localhost' -- /etc/hosts)
echo $'The \033[01m/etc/hosts\033[00m file contains\033[01m' \
    $NUM_INFO_LINES $'\033[00mlines pertaining to localhost \ 
    information, those lines are: '
cat ${TEMP_OUT}
echo


#============================================================================
# 5 - Display a list of /usr/share/doc subdirectories containing information about shells.
#============================================================================

echo $'The following is a list of "/usr/share/doc subdirectories \n'\
    '  containing information about shells:'
grep --fixed-strings --files-with-matches --binary-files=without-match --recursive  --regexp='shells' --file='/etc/shells' -- /usr/share/doc > ${TEMP_OUT}
switch_in_out
grep --only-matching --regexp='/.\+/' ${TEMP_IN} > ${TEMP_OUT}
switch_in_out
sort --unique ${TEMP_IN}
echo


#============================================================================
# 6 - Count the number of README files in the above mentioned subdirectories that have an ".md", ".txt" or no file extension at all.
#============================================================================

# NOTE: find is used for performance reasons.
# NOTE: need to add an explanation for what is going on here and do another version that doesn't rely on find but reuses the grep results from the previous section.
find /usr/share/doc -type f -a \( -ipath '*README*' -a \( \! -iname '*.*' -o \( -iname '*.txt' -o -iname '*.md' \) \) \) > ${TEMP_OUT}
switch_in_out
grep --only-matching --regexp='.\+/' ${TEMP_IN} > ${TEMP_OUT} 
switch_in_out
OPTIMIZED_DIR_LIST=$(sort --unique ${TEMP_IN}) grep --fixed-strings --files-with-matches --binary-files=without-match --recursive --regexp='shells' --file='/etc/shells' -- $OPTIMIZED_DIR_LIST > ${TEMP_OUT}
grep --only-matching --regexp='/.\+/' ${TEMP_IN} > ${TEMP_OUT}
unset -v OPTIMIZED_DIR_LIST
OPTIMIZED_DIR_LIST=$(sort --unique ${TEMP_IN})
grep --recursive --files-with-matches  --binary-files=without-match --regexp='' $OPTIMIZED_DIR_LIST > ${TEMP_OUT}
switch_in_out
grep --regexp='README' --ignore-case ${TEMP_IN} > ${TEMP_OUT}
switch_in_out
grep --extended-regexp --regexp='(README|\.md|\.txt)$' --ignore-case --count ${TEMP_IN} > ${TEMP_OUT}
NUM_README_FILES=$(cat ${TEMP_OUT})
echo $'In the abovementioned directories there are\033[01m' \
    $NUM_README_FILES $'\033[00mREADME files with a ".md" or' \
    'a ".txt" extension or no extension at all.'
echo


#============================================================================
# 7 - Display a list of files in the home directory that were changed less that 10 hours ago, using grep, but leave out directories.
#============================================================================

# NOTE: probably need to add an explanation for what is going here too.
echo -en {0,1,2,3,4,5,6,7,8,9}' hours ago\n' > ${TEMP_OUT}
switch_in_out
date --file=${TEMP_IN} +'%Y-%m-%d %H' > ${TEMP_OUT}
switch_in_out
VALID_DATE_STRINGS=$(paste --serial --delimiter='|' ${TEMP_IN}) 
ls --quote-name --time-style=long-iso --format=long --almost-all $HOME > ${TEMP_OUT}
switch_in_out
grep --extended-regexp --regexp="$VALID_DATE_STRINGS" ${TEMP_IN} > ${TEMP_OUT}
switch_in_out
grep --invert-match --regexp='^d' ${TEMP_IN} > ${TEMP_OUT}
switch_in_out
grep --extended-regexp --only-matching --regexp='".+"' ${TEMP_IN} > ${TEMP_OUT}
switch_in_out
echo 'The following is a list of files that have been changed in the last 10 hours:'
paste --serial --delimiter=',' ${TEMP_IN}
echo


