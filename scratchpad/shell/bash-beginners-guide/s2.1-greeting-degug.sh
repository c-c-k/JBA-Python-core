#!/usr/bin/env bash
#This script clears the terminal, shows a greeting, provides information about
#currently connected users, sets two variables and finnaly prints the values of
#said variables.

clear					# clear he terminal

echo "The script starts now"
set -v					# activate print commands from here

echo "Hi, $USER!"			# Dollar sign is used to get the content of a variable.
set +v					# stop print commands from here
echo 

echo "The files in the current folder are:"
set -o noglob				# disable globbing (filename generation using metacharacters)

echo ./*
set +o noglob				# enable globbing (filename generation using metacharacters)
echo

echo "I will now fetch you a list of connected users:"
echo
set -x					# activate debbuging from here

					# Show who is logged in
					# and what they are doing.
echo "debug message: now attempting to start the w program:";w

set +x					# stop debbuging from here
echo

echo "I'm setting the COLOUR and VALUE variables now."
COLOUR="black"				# Set a local shell variable
VALUE="9"				# Set a local shell variable
echo "The value of COLOUR is the string: $COLOUR"	# Display content of variable
echo "The value of VALUE is the number: $VALUE"	# Display content of variable
echo
echo "I'm giving you back your promp now."
echo
