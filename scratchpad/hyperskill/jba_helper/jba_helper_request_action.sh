#!/usr/bin/env bash

# jba_helper_request_action.sh
#
echo "$1;$2;" > "/dev/shm/jba_helper_action_request.writing"
mv "/dev/shm/jba_helper_action_request.writing" "/dev/shm/jba_helper_action_request"
sleep 0.5
