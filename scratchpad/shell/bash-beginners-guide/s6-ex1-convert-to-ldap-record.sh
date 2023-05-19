#!/usr/bin/env bash

set -x

# s6-ex1-convert-to-ldap-record.sh
# This script is a solution for the first exercise of chapter 6.
# First it generates a test data file with input lines in the following form:
# 
#   Username:Firstname:Lastname:Telephone number
# 
# Then it calls the awk script "s6-ex1-convert-to-ldap-record.awk" to convert
# each such line to an LDAP record in the following format:
# 
#    dn: uid=Username, dc=example, dc=com
#    cn: Firstname Lastname
#    sn: Lastname
#    telephoneNumber: Telephone number

# -- Set variables for script and data file paths --
DATA_FILE="/dev/shm/test-data-$$-$(date +%s).tmp"
SCRIPT_FILE=./s6-ex1-convert-to-ldap-record.awk
# -- prepare test data --
echo -n $'username1:firstname1:lastname1:001122334401\n'\
$'username2:firstname2:lastname2:001122334402\n'\
$'username3:firstname3:lastname3:001122334403\n'\
$'username4:firstname4:lastname4:001122334404\n'\
$'username5:firstname5:lastname5:001122334405\n'\
> $DATA_FILE
cat $DATA_FILE
# -- execute awk script
awk --file="$SCRIPT_FILE" -- $DATA_FILE
# -- cleanup
rm --force $DATA_FILE
unset -v DATA_FILE SCRIPT_FILE

