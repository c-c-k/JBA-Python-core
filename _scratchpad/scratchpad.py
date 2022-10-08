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

# Write a program that reads a user's name from input and prints the
# following message: Dear <username>! It was really nice to meet you.
# Hopefully, you have a nice day! See you soon, <username>!. Change the word
# <username> with the word that is provided in the input. We recommend using
# string templates from the string module to complete the task.

# ---- code start ----
import string
template = string.Template(
    "Dear $username! It was really nice to meet you. "
    "Hopefully, you have a nice day! See you soon, $username!")
username = input()
print(template.substitute(username=username))
