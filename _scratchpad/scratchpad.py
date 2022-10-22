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

# Mr. and Ms. Smith
# Medium
# 1191 users solved this problem. Latest completion was about 4 hours ago.
# 
# Let's try to differentiate between some kinds of honorifics. Write a
# regular expression in the variable template in such a way that it would
# match the following strings:
# 
# Mr Smith
# Mr. Smith
# Ms Smith
# Ms. Smith
# 
# Note that your template should not match any other strings (for example,
# Dr. Smith).

# ---- code start ----
import re
# define regex template
template = r'M[rs]\.? Smith'
