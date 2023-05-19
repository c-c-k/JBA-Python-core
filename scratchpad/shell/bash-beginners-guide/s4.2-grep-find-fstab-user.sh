#!/usr/bin/env bash

# This script user the ${!} mechanism and grep to output a message whether a
# given user exists in "/etc/fstab"

# For the purpose of this practice script the user name to be checked is
# placed in the script itself.
TESTED_USER_NAME='root'

# This line uses grep to search "/etc/fstab" for a line begining with exactly
# the given username.
USER_NAME_LINE_COUNT=$(grep --count --max-count=1 --regexp="^$TESTED_USER_NAME\:" /etc/passwd)

# The following two lines prepare the two possible output messages.
MSG1="The user ${TESTED_USER_NAME} exists in \"/etc/passwd\""
MSG0="The user ${TESTED_USER_NAME} does not exists in \"/etc/passwd\""

# This line selects the message to be printed.
MSG_SWITCH=MSG${USER_NAME_LINE_COUNT}

#This line uses the ${!} mechanism to print the relevant message.
echo ${!MSG_SWITCH}


