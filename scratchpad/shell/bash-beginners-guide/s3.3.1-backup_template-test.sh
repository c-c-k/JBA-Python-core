#!/usr/bin/env bash

# backup_template_example.sh
# This script backs up preset files in a preset directory to a server with an
# ssh key access.

# Modify these variables to change what gets backed up and to where.
BACKUP_ROOT_DIR=/home/cck-su/Documents/scans/internet_and_shopping/food_tools_pharm/
FILES_TO_BACKUP=2022
TAR_FILE_PATH=/var/tmp/backuptest.tar
GZIP_FILE_PATH=/var/tmp/backuptest.tar.gz
BACKUP_SERVER_ADDRESS=ssh-localhost
BACKUP_SERVER_PATH=/dev/shm/
LOG_FILE_PATH=/dev/shm/templogfile.log

# This switches to the intended backup root dir.
cd $BACKUP_ROOT_DIR

# This creates the archive
tar -cf $TAR_FILE_PATH $FILES_TO_BACKUP > /dev/null 2>&1

# This removes the old compressed file and then creates a new one. Errors are
# redirected because some would be generated if the old gzip file doesn't
# exist.
rm $GZIP_FILE_PATH 2> /dev/null
gzip $TAR_FILE_PATH

# This copies the compressed file to the backup server. An ssh key is used to
# avoid the need for manual intervention during login.
scp $GZIP_FILE_PATH $BACKUP_SERVER_ADDRESS:$BACKUP_SERVER_PATH > /dev/null 2>&1

# This creates a record in the log file.
date >> $LOG_FILE_PATH
echo backup succeeded >> $LOG_FILE_PATH

