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

# Cities
# Medium
# 13798 users solved this problem. Latest completion was about 7 hours ago.
# 
# Imagine you've created a program that plays the cities game with a user.
# For the game to work, you need to remember the user's city and be able to
# change it. Below is the code that does that, but if you run it as is,
# you'll get an error: you won't be able to access the variable user_city
# outside of the function. Fix this problem by adding one line. Please, don't
# change the rest of the code.

# ---- code start ----
def change_city(new_user_city):
    global user_city
    user_city = new_user_city


change_city("Paris")
print(user_city)
