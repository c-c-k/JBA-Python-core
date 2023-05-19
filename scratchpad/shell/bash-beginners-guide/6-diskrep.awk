BEGIN { print "*** WARNING WARNING WARNING ***"}
/\<(100|[5-9][[:digit:]])%/ { print "Partition " $6 " is " $5 " full"}
END { print "*** Consider buying new storage hardware ***"}
