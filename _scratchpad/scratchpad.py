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

# Reverse
# Medium
# 5705 users solved this problem. Latest completion was 1 day ago.
# 
# In this task, we have a list numbers = [2, 4, 6, ...] and a line that is
# supposed to choose elements with indices from 4 to 16 inclusively in reverse
# order, but a mistake has been made. Find and fix it.
# 

# ---- code start ----
# the following line reads the list from the input; do not modify it, please
numbers = [int(num) for num in input().split()]
print(numbers[16:3:-1])  # the line with an error
