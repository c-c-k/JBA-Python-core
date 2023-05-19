#!/usr/bin/env bash

set -x

# s7-conditional-examples.sh
# These are the example scripts given in the body of chapter 7.

#----------------------------------------------------------
# 7.1.1.3 - Checking files.
#----------------------------------------------------------
# -- Prepare example data --
# -- Example commands --
chmod u+x ./s7-msgcheck.sh
./s7-msgcheck.sh
# -- Clean example data --
# -- Print a separator before the next example --
echo $'\n\n'


#----------------------------------------------------------
# 7.1.1.4 - checkig shell options
#----------------------------------------------------------
# -- Prepare example data --
set -o noclobber
# -- Example commands --
if [ -o noclobber ]
then
    echo "your files are protected against overwriting"
fi
if [ -o noclobber ]; then echo "your files are protected against overwriting"; fi;
# -- Clean example data --
set +o noclobber
# -- Print a separator before the next example --
echo $'\n\n'


#----------------------------------------------------------
# 7.1.2.1 - testing exit status
#----------------------------------------------------------
# -- Prepare example data --
# -- Example commands --
ls / > /dev/null
if [ $? -eq 0 ]
then echo 'Process completed without errors'
fi
if ! ls /nonexistantdir; then echo "process failed, however the exit status got lost because it changed to the exit status of the if conditional which is : $?"; fi
ls /nonexistantdir
COMMAND_EXIT_STATUS=$?
if [ $COMMAND_EXIT_STATUS -ne 0 ]
then echo "Process failed with exit status $COMMAND_EXIT_STATUS"
fi
# -- Clean example data --
# -- Print a separator before the next example --
echo $'\n\n'


#----------------------------------------------------------
# 7.1.2.2 - Numeric comparisons
#----------------------------------------------------------
# -- Prepare example data --
# -- Example commands --
WORK_HOURS=200
if [ "$WORK_HOURS" -lt "1000" ]
then echo 'no rest for the weary no redemption for the wicked'
fi
# -- Clean example data --
# -- Print a separator before the next example --
echo $'\n\n'
exit


#----------------------------------------------------------
# 7.
#----------------------------------------------------------
# -- Prepare example data --
# -- Example commands --
# -- Clean example data --
# -- Print a separator before the next example --
echo $'\n\n'


#----------------------------------------------------------
# 7.
#----------------------------------------------------------
# -- Prepare example data --
# -- Example commands --
# -- Clean example data --
# -- Print a separator before the next example --
echo $'\n\n'


#----------------------------------------------------------
# 7.
#----------------------------------------------------------
# -- Prepare example data --
# -- Example commands --
# -- Clean example data --
# -- Print a separator before the next example --
echo $'\n\n'


#----------------------------------------------------------
# 7.
#----------------------------------------------------------
# -- Prepare example data --
# -- Example commands --
# -- Clean example data --
# -- Print a separator before the next example --
echo $'\n\n'


#----------------------------------------------------------
# 7.
#----------------------------------------------------------
# -- Prepare example data --
# -- Example commands --
# -- Clean example data --
# -- Print a separator before the next example --
echo $'\n\n'


#----------------------------------------------------------
# 7.
#----------------------------------------------------------
# -- Prepare example data --
# -- Example commands --
# -- Clean example data --
# -- Print a separator before the next example --
echo $'\n\n'


#----------------------------------------------------------
# 7.
#----------------------------------------------------------
# -- Prepare example data --
# -- Example commands --
# -- Clean example data --
# -- Print a separator before the next example --
echo $'\n\n'


