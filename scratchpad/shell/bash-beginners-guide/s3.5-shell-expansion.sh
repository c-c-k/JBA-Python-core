#!/usr/bin/env bash

# s3.5-shell-expansion.sh
# This script checks and demonstrated the 8 different types of expansion
# performed by the bash shell in the order in which they are performed.

set -o verbose  # Lazy way to print the remarks in the output.
# ----- ALIASES -----
# alias definition should always be single qouted to avoid word splitting
# strangeness.
shopt -s expand_aliases
shopt |grep alias
alias echo='echo "<STDOUT>:"'


# ----- 1. BRACE EXPANSION -----
# The first type of expansion performed is brace ({}) expansion. Values inside
# braces are expanded to a list of words in which the prefix and the suffix to
# the braces is added to each of the values within them.
# Don't forget to take note on the effect of spaces on word boundaries.
# Generally any malformed brace expression is left unchanged.
echo 'I saw a '{c,r,b,m}at.
echo 'I saw a' {c,r,'b ',m}at .
echo 'I saw a' {c,r,b ,m}at .
echo I saw a '{'c,r,b,m}at.
echo I saw a {'c,r,b,m'}at.
# Also note that an unquoted space inside the braces breaks things.
# And also note that ${ performs parameter expansion and is thus not eligible
# for brace expansion. 
b=2;c=$b;m='magenta';r='rainbow'
echo 'I saw a $'{c,r,b,m}at.
echo 'I saw a '${c,r,b,m}at.
# Braces can be nested, the results are not sorted, left to right order is
# preserved.
echo a{1,2,3}b c{5,4,6{.8,.2,.3{9,6,3}}}d
# Brace expansion is strictly textual and performed first, thus characters
# that have a special meaning to other expansions are preserved in the result.
echo 'I saw a '{$c,$r,$b,$m,~/}
unset -v c r m b


# ----- 2. TILDE EXPANSION -----
# $HOME expansion
echo ~ , ~root , ~irc
# expands to slash
echo ~/path/to/folder
# non-existing user will leave the tilde expression unchanged
echo ~non_existing_user09540437505780
# can be used for variable assignment due to expansion after ":" and "="
# characters
DEMOPATH=~
echo $DEMOPATH
DEMOPATH=~:~irc
echo $DEMOPATH
DEMOPATH=~root:$DEMOPATH
echo $DEMOPATH
# double quotes negate tilde special meaning
DEMOPATH+="~root"
echo $DEMOPATH
echo "~"
DEMOPATH="~"
echo $DEMOPATH
unset -v DEMOPATH
# also can be used with dirstack using ~n ~+n ~-n syntax
pushd -n ~ > /dev/null
pushd -n ~root > /dev/null
pushd -n ~/Documents > /dev/null
pushd -n ~bin > /dev/null
dirs -v
echo ~0
echo ~1
echo ~+3
echo ~-0
echo ~-1
echo ~-3
# also ~+ expands to $PWD and ~- expands to $OLDPWD
cd /usr/bin
echo ~+ , ~-
cd -
echo ~+ , ~-

# ----- 3. SHELL PARAMETER AND VARIABLE EXPANSION -----
bash -c "echo \$0 '<STDOUT>:' \$9 \$10 \$11" 'subshell' a 2 3 4 5 6 7 8 9 10 11 12
bash -c "echo \$0 '<STDOUT>:' \${9} \${10} \${11}" 'subshell' a 2 3 4 5 6 7 8 9 10 11 12
echo `DEMOVARIABLE_1='--DEMOVALUE_1--'` 
# !!! doesn't work because backtick opens a subshell !!!
echo DEMOVARIABLE_2='--DEMOVALUE_2--' 
# !!! doesn't work because DEMOVALUE_2 is treated as simple text !!!
echo ${DEMOVARIABLE_3:='--DEMOVALUE_3--'}
echo ${1:='--DEMOVALUE_3--'}
1='--DEMOVALUE_3--'
DEMOVARIABLE_4=DEMOVARIABLE_1
echo ${!DEMOVARIABLE_4}
echo $DEMOVAR*
# !!! doesn't work because $DEMOVAR is treated as a nonexistent variable and * is treated seperately and thus globed!!!
echo $DEMOVARIABLE_{1,2,3,4}
echo ${!DEMOVAR*}
bash -c "echo \$0 '<STDOUT>:' \${!DEMOVAR*}" 'subshell'
export ${!DEMOVAR*}
bash -c "echo \$0 '<STDOUT>:' \${!DEMOVAR*}" 'subshell'
export -n ${!DEMOVAR*}
bash -c "echo \$0 '<STDOUT>:' \${!DEMOVAR*}" 'subshell'
unset -v ${!DEMOVAR*}
echo ${!DEMOVAR*}
${DEMOVAR:='demoval'}
echo $DEMOVAR
unset -v ${!DEMOVAR*}
echo $DEMOVAR
DEMOVAR1='demoval'
DEMOVAR2=0
DEMOVAR3=2
echo ${DEMOVAR2+($DEMOVAR1)}

# ----- 4. COMMAND SUBSTITUTION -----
echo date
echo `date`
echo $(date)
#echo `\$PWD date`
#echo `$PWD date`
#echo $(\$PWD date)
#echo $($PWD date)

# ----- 5. ARITHMETIC EXPANSION -----
echo ${VALUE_1:=2},${VALUE_2:=13}
echo $((VALUE_2%VALUE_1))
echo $(($VALUE_2%$VALUE_1))
echo $[VALUE_2%VALUE_1]
echo $[$VALUE_2%$VALUE_1]
echo $[VALUE_1++]
echo $[VALUE_1]
echo $[++VALUE_1]
echo $[2<<VALUE_1]
echo $[VALUE_2||11]
echo $[VALUE_2|11]
echo $[VALUE_2|19]
echo $[VALUE_2&&11]
echo $[VALUE_2&11]
echo $[VALUE_2&19]
echo $[VALUE_2^11]
echo $[VALUE_2^19]
unset -v ${!VALUE_*}

# ----- 6. PROCESS SUBSTITUTION -----
# need to get a grip on named pipes (FIFO's) first.

# ----- 7. WORD SPLITTING -----
echo $(set|grep ^IFS)
bash -c 'echo \<STDOUT\>\: \$\#\=$#' 'test' "a b c"
bash -c 'echo \<STDOUT\>\: \$\#\=$#' 'test' a b c
bash -c 'echo \<STDOUT\>\: \$\#\=$#' 'test' a	b	c
bash -c 'echo \<STDOUT\>\: \$\#\=$#' 'test' a b\nc
bash -c 'echo \<STDOUT\>\: \$\#\=$#' 'test' a$'\n'b$'\t'c
bash -c 'echo \<STDOUT\>\: \$\#\=$#' 'test' a$''b$''c
bash -c 'echo \<STDOUT\>\: \$\#\=$#' 'test' """" "''"
bash -c 'echo \<STDOUT\>\: \$\#\=$#' 'test' "" ''
VALUE_1='value'
VALUE_2=""""
bash -c 'echo \<STDOUT\>\: \$\#\=$#' 'test' $VALUE_1 $VALUE_2 $VALUE_3
bash -c 'echo \<STDOUT\>\: \$\#\=$#' 'test' "$VALUE_1" "$VALUE_2" "$VALUE_3"
unset -v ${!VALUE_*}
echo $(set|grep [NTSU][12]?)
echo ${PPPN:=$'\n'} , ${PPPT:=$'\t'} , ${PPPS:=$' '} , ${PPPF:=$'\f'} , ${PPPU1:=''} , ${PPPU2:=""}
echo $(set|grep ^PPP)
bash -c 'echo \<STDOUT\>\: \$\#\=$#' 'test' a${PPPS}b
bash -c 'echo \<STDOUT\>\: \$\#\=$#' 'test' a${PPPN}b
bash -c 'echo \<STDOUT\>\: \$\#\=$#' 'test' a${PPPT}b
bash -c 'echo \<STDOUT\>\: \$\#\=$#' 'test' a${PPPU1}b
bash -c 'echo \<STDOUT\>\: \$\#\=$#' 'test' a${PPPU2}b
bash -c 'echo \<STDOUT\>\: \$\#\=$#' 'test' a${PPPT}${PPPN}${PPPS}b
bash -c 'echo \<STDOUT\>\: \$\#\=$#' 'test' ${PPPT} ${PPPN} ${PPPS}
bash -c 'echo \<STDOUT\>\: \$\#\=$#' 'test' ${PPPU1} ${PPPU1}
bash -c 'echo \<STDOUT\>\: \$\#\=$#' 'test' a${PPPT}${PPPN}${PPPS}${PPPF}${PPPT}${PPPN}${PPPS}b
IFS=$' \t\n\f'
echo $(set|grep ^IFS) , ${!PPP*}
echo  \${${!PPP*}}
# doesn't work because brace expansion happens first while ${!PPP*} only gets
# expanded later during variable expansion.
bash -c 'echo \<STDOUT\>\: \$\#\=$#' 'test' a${PPPT}${PPPN}${PPPS}${PPPF}b
bash -c 'echo \<STDOUT\>\: \$\#\=$#' 'test' a${PPPT}${PPPN}${PPPS}${PPPF}${PPPT}${PPPN}${PPPS}b
unset ${!PPP*} $IFS
echo $(set|grep ^IFS) , ${!PPP*}

# ----- 8. FILE NAME EXPANSION -----
touch file-a
touch file-B
touch file-c
touch file-D
touch .file-e
touch .ile-f
set -o noglob
echo file*
set +f
echo file*
echo file?
shopt -s nullglob
echo file?
shopt -u nullglob
echo file-?
echo file-[abc]
shopt -s nocaseglob
echo file-[abc]
shopt -u nocaseglob
echo file-[cef]
echo .ile-[cef]
echo ?ile-[cef]
shopt -s dotglob
echo .ile-[cef]
echo ?ile-[cef]
shopt -u dotglob
shopt dotglob
GLOBIGNORE='*-a'
shopt dotglob
echo .ile-[cef]
echo ?ile-[cef]
echo file*
echo *file*
GLOBIGNORE=$GLOBIGNORE:'.*'
echo *file*
echo .file*
shopt dotglob
unset -v GLOBIGNORE
shopt dotglob
echo *file*
echo .file*
echo 'with clobber' > file-a
cat file-a
set -o noclobber
echo 'the old clobber that is' >> file-a
echo 'without clobber' > file-a
cat file-a
set +o noclobber
shopt -s dotglob
echo *ile-*
rm [.f]ile-[aBcDf] .file-e
echo *ile-*

set -u  # generates an error for non existing variables, quits non iteractive scripts on said error.
echo $NONEXISTINGVAR

# This line shall not be reached.
set +o verbose
