#   Precede all symlink lines with the line "--This is a symlink--" and
/^l/i\
\
	--This is a symlink--
#   Follow symlink lines with the line "---------------------". 
/^l/a\
	---------------------\

#   Suffix all lines with a plain file with: "<--- this is a plain file".
s/^-.*/&  <--- this is a plain file/
