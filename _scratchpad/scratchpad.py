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

# We Are What We Eat
# Medium
# 4304 users solved this problem. Latest completion was about 17 hours ago.
# 
# Anthony keeps track of what he eats: he writes down how many calories are in
# his meals. Use the list of dictionaries to calculate the total amount of
# calories per day and print it.
# 
# The sample input will look like:
# 
# meals = [
# {"title": "Oatmeal pancakes with apple and cinnamon", "kcal": 370},
# {"title": "Italian salad with fusilli and ham", "kcal": 320},
# {"title": "Bulgur with vegetables", "kcal": 350},
# {"title": "Curd souffle with lingonberries and ginger", "kcal": 225},
# {"title": "Oatmeal with honey and peanuts", "kcal": 440}]
# 
# The output in this case should be 1705.
# 

# ---- code start ----
# the list "meals" is already defined
# your code here
# meals = [
#     {"title": "Oatmeal pancakes with apple and cinnamon", "kcal": 370},
#     {"title": "Italian salad with fusilli and ham", "kcal": 320},
#     {"title": "Bulgur with vegetables", "kcal": 350},
#     {"title": "Curd souffle with lingonberries and ginger", "kcal": 225},
#     {"title": "Oatmeal with honey and peanuts", "kcal": 440}]

print(sum([meal["kcal"] for meal in meals]))