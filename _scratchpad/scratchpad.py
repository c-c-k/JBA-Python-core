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

# The Law of Sines
# Hard
# 355 users solved this problem. Latest completion was 32 minutes ago.
# 
# There is a triangle on the picture below with the following parameters:
# 
# - angle A and sides a and c are unknown;
# 
# - angle B = 35°, angle C = 105°, side b = 7.
# 
# Find the side c using the math module. Print the answer rounded to 1
# decimal place.
# 

# ---- code start ----
import math

angle_b = 35
angle_c = 105
# sum of angles in triangle: A = 180 - B - C
angle_a = 180 - angle_b - angle_c

side_b = 7
# law of sines: b/sin(B) = c/sin(C)
#               c = (b*sin(C))/sin(B)
angle_c = math.radians(angle_c)
angle_b = math.radians(angle_b)
side_c = round((side_b * math.sin(angle_c)) / math.sin(angle_b), 1)
print(side_c)
