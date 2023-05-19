#!/usr/bin/env bash

# This script prints the current users home directory and terminal type,
# as well as a list of all services started at run level 3.

# Clearing the screen to avoid clatter.
clear

# Print the users home directory.
echo "The users home directory is: $HOME"	# Could have also used "~"
						# but $HOME is more clear.
echo

# Print the users terminal type (not to be confused with shell type).
echo "The type of the currently active terminal is: $TERM"
echo

# Print a list of all services started at run level 3.
echo "Currently the services started at run level 3 are:"
ls /etc/rc3.d/*
