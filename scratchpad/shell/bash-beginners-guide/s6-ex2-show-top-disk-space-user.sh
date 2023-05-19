#!/usr/bin/env bash

set -x

# s6-ex2-show-top-disk-space-user.sh
# Create a Bash script using awk and standard UNIX commands that will
# show the top three users of disk space in the /home file system (if you
# don't have the directory holding the homes on a separate partition, make
# the script for the / partition; this is present on every UNIX system).
# First, execute the commands from the command line. Then put them in a
# script. The script should create sensible output (sensible as in readable
# by the boss). If everything proves to work, have the script email its
# results to you (use for instance mail -s Disk space usage <you@your_comp> <
# result).
# 
# If the quota daemon is running, use that information; if not, use find.
