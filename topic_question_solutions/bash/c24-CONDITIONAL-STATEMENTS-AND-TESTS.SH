#!/usr/bin/env bash

function tri() {
  if [ $(( $1 + $2 + $3 )) -eq "180" ]; then
      echo "Yes"
  else
      echo "No"
  fi
}

function essay() {
  if [ "$1" -gt "500" ] && [ "$1" -lt "1000" ]; then
      echo "Good Job!"
  else
      echo "Revise the essay"
  fi
}

function password() {
  if [ "$1" = "$2" ]; then
      echo "Correct password entered. Proceeding further"
  else
      echo "Incorrect password. Please try again"
  fi
}

function file_exist() {
  if [ ! -e "$1" ]; then
    echo "File does not exist"
  elif [ ! -s "$1" ]; then
    echo "File exists but is empty"
  else
    echo "File exists and is not empty"
  fi
}
file_exist "$@"