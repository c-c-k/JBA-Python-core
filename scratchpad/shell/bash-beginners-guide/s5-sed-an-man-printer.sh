#!/usr/bin/env bash

# s5-sed-an-man-printer.sh
# This script does the following:
# 1.  Prints a list of files in this directory, ending in ".sh". Unaliasing ls
#     to be on the safe side. The results are saved to the temporary file
#     "/dev/shm/sed.ex1.tmp.
# 2.  Makes a list of files in "/usr/bin" that have the letter "a" as the
#     second character. The results are saved to the temporary file
#     "/dev/shm/sed.ex2.tmp.
# 3.  Deletes the first 3 lines of each temporary file.
# 4.  Prints to standard output only the lines containing the pattern "an".
# 5.  Adds a the string "*** This might have something to do with man and man
#     pages ***" in the line preceding every occurence of the string "man".

#----------------------------------------------------------------------------
# 1.  Print a list of files in this directory, ending in ".sh". Unaliasing ls
#     to be on the safe side. The results are saved to the temporary file
#     "/dev/shm/sed.ex1.tmp.
#----------------------------------------------------------------------------
unalias ls
echo $'Printing and saving to a temporary file all files ending in ".sh"\n in the current directory: '
ls ~/bpg | sed --silent --expression='/\.sh/p' > /dev/shm/sed.ex1.tmp
cat "/dev/shm/sed.ex1.tmp"
echo $'-----DONE------\n\n'


#----------------------------------------------------------------------------
# 2.  Make a list of files in "/usr/bin" that have the letter "a" as the
#     second character. The results are saved to the temporary file
#     "/dev/shm/sed.ex2.tmp.
#----------------------------------------------------------------------------
echo $'Saving to a temporary file a list of all files in the "/usr/bin" \ndirectory with the character "a" as the second in their name...'
ls /usr/bin | sed --quiet --expression='/^.a.*/p' > /dev/shm/sed.ex2.tmp
echo $'-----DONE------\n\n'


#----------------------------------------------------------------------------
# 3.  Delete the first 3 lines of each temporary file.
#----------------------------------------------------------------------------
echo $'Removing the first 3 lines of each of the above temporary files...'
sed --separate --in-place='.backup' --expression='1,3d' /dev/shm/sed.ex?.tmp
echo $'-----DONE------\n\n'


#----------------------------------------------------------------------------
# 4.  Print to standard output only the lines containing the pattern "an".
#----------------------------------------------------------------------------
echo $'Printing only the lines containing the pattern "an" from the above \ntemporary files'
sed --separate --silent --expression='/an/p' /dev/shm/sed.ex?.tmp
echo $'-----DONE------\n\n'


#----------------------------------------------------------------------------
# 5.  Add a the string "*** This might have something to do with man and man
#     pages ***" in the line preceding every occurence of the string "man".
#----------------------------------------------------------------------------
echo $'Adding the line "*** This might have something to do with man and man \npages ***" before every line containing the string "man"'
sed --in-place --separate --expression='/man/i*** This might have something to do with man and man pages ***' --expression='/man/a^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^' --expression='s/.*man.*/--->&<---/' /dev/shm/sed.ex?.tmp
cat /dev/shm/sed.ex?.tmp
echo $'-----DONE------\n\n'
