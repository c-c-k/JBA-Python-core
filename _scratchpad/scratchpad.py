# # !/usr/bin/env python3.10
# # -*- coding: utf-8 -*-
# 
# """Scratch pad for Jet Brains Academy topic questions.
# 
# Properly formatting and saving the solutions for the topic practice
# questions
# feels like a waste of time, so instead I decided to use this script for
# copying and pasting and editing the script and then copying the solution to
# solutions_dump.
#

# Nursery rhymes
# Hard
# 598 users solved this problem. Latest completion was about 12 hours ago.
# 
# Imagine you have to write a poem for kids about animals. You struggle with
# finding appropriate rhymes for the word bunny. Write a regexp pattern that
# will match the right words: they should be from 4 to 7 letters long and end
# with -nny or -ney. Note that the pattern should only match strings containing
# letters—for example, the string 123nny should not be considered a good
# result.
# 
# Put your regexp in the template variable. You do NOT need to print any
# results.

# ---- code start ----
import re
# put your regex in the variable template
template = "[a-zA-Z]{1,4}n[en]y"
