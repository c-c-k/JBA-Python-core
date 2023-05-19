#!/usr/bin/env bash

# c19-CASE_STATEMENTS.sh
#

function court() {
  case "$1" in
    'G' | 'g' )
      echo "The defendant is guilty." ;;
    'N' | 'n')
      echo "The defendant is not guilty." ;;
    'P' | 'p')
      echo "The trial has been postponed." ;;
    *)
      echo "Order Order!" ;;
  esac
}
#court "$@"

function skipper() {
    # put your code here
    for (( ; 0 < "$#" ; ))
    do
      case "${1}" in
        0 )
          exit ;;
        1 | 2 | 3 )
          echo "$1"
          if [ "$#" -gt "$1" ] ; then
              shift "$1"
            else
              shift "$#"
          fi
          ;;
        * )
          shift 1  # dispose of illegal input
          ;;
      esac
    done
}
skipper "$@"
