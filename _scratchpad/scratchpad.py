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

# Full name
# Medium
# 5154 users solved this problem. Latest completion was about 4 hours ago.
# 
# Rewrite the code below using the with keyword.
# 
# Make sure to use the same variable names for file objects!

# ---- code start ----
with open('name.txt') as f1, open('surname.txt') as f2, open('full_name.txt', 'w') as f3:
    f3.write(' '.join([f1.read(), f2.read()]))
