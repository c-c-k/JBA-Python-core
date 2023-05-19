BEGIN { OFS="-" ; ORS="\n-->\n" }
{ print "Record number " NR ":\t" $1, $2 }
END { print "Total number of records:\t" NR}
