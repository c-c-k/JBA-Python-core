#!/usr/bin/env bash

set -x

# s6-info-awk-examples.sh
# This is a copy of the examples presenteed on the awk info pages.

#----------------------------------------------------------
# Bad usage of the -e (--source) option
#----------------------------------------------------------
# -- Prepare example data --
# -- Example commands --
awk -e 'BEGIN { a=5 ; print a }'  # this is correct.
awk -e 'BEGIN { a=5 }' -e 'BEGIN { print a }'  # this is also correct.
awk -e 'BEGIN { a=5 ; ' -e ' print a }'  # this is not correct but will work in
					 # gawk versions prior to version 5.
# -- Clean example data --
# -- Print a separator before the next example --
echo $'\n\n'


#----------------------------------------------------------
# Include (@include) command examples
#----------------------------------------------------------
# -- Prepare example data --
echo $AWKPATH
echo $'BEGIN {\n\tprint "This is script test1" \n}' > ./info-awk-test1
echo $'@include "info-awk-test1"\nBEGIN {\n\tprint "This is script test2" \n}' > ./info-awk-test2
echo $'@include "info-awk-test2"\nBEGIN {\n\tprint "This is script test3" \n}' > ./info-awk-test3
cat ./info-awk-test?
# -- Example commands --
gawk -f info-awk-test3
# -- Clean example data --
rm ./info-awk-test?
# -- Print a separator before the next example --
echo $'\n\n'


#----------------------------------------------------------
# Loading dynamic extensions
#----------------------------------------------------------
# -- Prepare example data --
# -- Example commands --
gawk '@load "ordchr"; BEGIN {print chr(65)}'
gawk -l"ordchr" ' BEGIN {print chr(66)}'
# -- Clean example data --
# -- Print a separator before the next example --
echo $'\n\n'

exit

#----------------------------------------------------------
# 
#----------------------------------------------------------
# -- Prepare example data --
# -- Example commands --
# -- Clean example data --
# -- Print a separator before the next example --
echo $'\n\n'


#----------------------------------------------------------
# 
#----------------------------------------------------------
# -- Prepare example data --
# -- Example commands --
# -- Clean example data --
# -- Print a separator before the next example --
echo $'\n\n'


#----------------------------------------------------------
# 
#----------------------------------------------------------
# -- Prepare example data --
# -- Example commands --
# -- Clean example data --
# -- Print a separator before the next example --
echo $'\n\n'


#----------------------------------------------------------
# 
#----------------------------------------------------------
# -- Prepare example data --
# -- Example commands --
# -- Clean example data --
# -- Print a separator before the next example --
echo $'\n\n'


#----------------------------------------------------------
# 
#----------------------------------------------------------
# -- Prepare example data --
# -- Example commands --
# -- Clean example data --
# -- Print a separator before the next example --
echo $'\n\n'


#----------------------------------------------------------
# 
#----------------------------------------------------------
# -- Prepare example data --
# -- Example commands --
# -- Clean example data --
# -- Print a separator before the next example --
echo $'\n\n'


#----------------------------------------------------------
# 
#----------------------------------------------------------
# -- Prepare example data --
# -- Example commands --
# -- Clean example data --
# -- Print a separator before the next example --
echo $'\n\n'


#----------------------------------------------------------
# 
#----------------------------------------------------------
# -- Prepare example data --
# -- Example commands --
# -- Clean example data --
# -- Print a separator before the next example --
echo $'\n\n'


