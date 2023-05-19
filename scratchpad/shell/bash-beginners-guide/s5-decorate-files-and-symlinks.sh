#!/usr/bin/env bash

# s5-decorate-files-and-symlinks.sh
# 6. Using a long listing of the home directory "~" as input. The sed script
#    file "s5-decorate-files-and-symlinks.sed" is used to:
#	i.	Precede all symlink lines with the line "--This is a symlink--" and
#		follow it with the line "---------------------". 
#	ii.	Suffix all lines with plain file with: "<--- this is a plain file".


ls --almost-all --format=long ~ | sed --file=s5-decorate-files-and-symlinks.sed
