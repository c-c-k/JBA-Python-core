# precede a line with trailing blanks with a message to the effect.
/[[:blank:]]\+$/i\
    --- The following line has trailing spaces: ---
# Use regex substitution with ANSI escape codes to make the blanks clearyly visible.
/[[:blank:]]\+$/s/\(.*[^[:blank:]]\|\)\([[:blank:]]\+$\)/\1[04;07m>>\2<<[00m/
/[[:blank:]]\+<<\[00m$/p

