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

# Zero
# Medium
# 5707 users solved this problem. Latest completion was 40 minutes ago.
# 
# Prevent ZeroDivisionError in the code below. When denominator is 0, print
# the message "Division by zero is not supported". In other cases, print n
# divided by denominator.

# ---- code start ----
n = int(input())
denominator = int(input())
try:
    print(n // denominator)
except ZeroDivisionError:
    print("Division by zero is not supported")
