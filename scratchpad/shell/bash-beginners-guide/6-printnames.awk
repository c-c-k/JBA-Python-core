BEGIN { FS=":" }
/bash/ { print $1 "\t" $5 }
