#!/usr/bin/env bash
#
# s7-msgcheck.sh

#echo "This script checks for the existance of the messages file."
echo "This script checks for the existance of a .vimrc file."
echo "checking..."
if [ -f ~/.vimrc ]
    then
	echo "$HOME/.vimrc exists."
fi
echo
echo "Done.."
