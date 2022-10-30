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

# Restaurant
# Medium
# 1932 users solved this problem. Latest completion was 3 days ago.
# 
# Imagine you are having dinner in a very fancy restaurant, but unfortunately
# you don't have a lot of money with you. You want to have a main course, a
# dessert and a drink, but all that together shouldn't cost more than $30.
# 
# The names of the main courses, desserts and drinks are stored in the lists
# main_courses, desserts and drinks respectively. The corresponding prices
# can be found in the lists price_main_courses, price_desserts and
# price_drinks.
# 
# Consider each possible combination of a main course, dessert and a drink
# from those offered by the restaurant and print out only those meals that
# satisfy your budget, along with their total costs.
# 
# For instance, imagine the dishes and prices are as defined below:
# 
# main_courses = ['beef stew', 'fried fish']
# price_main_courses = [28, 23]
# 
# desserts = ['ice-cream', 'cake']
# price_desserts = [2, 4]
# 
# drinks = ['cola', 'wine']
# price_drinks = [3, 10]
# 
# Then, your output should be the following:
# 
# fried fish ice-cream cola 28
# fried fish cake cola 30
# 

# ---- code start ----
import itertools
MONEY = 30
# main_courses = ['beef stew', 'fried fish']
# price_main_courses = [28, 23]
# desserts = ['ice-cream', 'cake']
# price_desserts = [2, 4]
# drinks = ['cola', 'wine']
# price_drinks = [3, 10]

for diner, diner_costs in zip(
    itertools.product(main_courses, desserts, drinks),
    itertools.product(price_main_courses, price_desserts, price_drinks)
):
    diner_total_cost = sum(diner_costs)
    if diner_total_cost <= MONEY:
        print(" ".join(diner), diner_total_cost)
