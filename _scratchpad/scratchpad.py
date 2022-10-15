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


# Temperature
# Hard
# 8114 users solved this problem. Latest completion was 1 day ago.
# 
# Below you can see a draft of a program for a basic temperature converter from
# Fahrenheit to Celsius and vice versa. You need to finish the program by
# creating a sort of entry point for the program in the function main.
# 
# In this function, you should:
# 
# process the input. The input is a string containing a temperature value and a
# unit of measurement which are separated by a whitespace character. We already
# wrote the code that reads the input and creates the variables, but you still
# need to figure out what the right type is for each of them and convert if
# necessary;
# call the appropriate function depending on what was given in the input;
# print the converted temperature with the new unit.
# 
# Use the examples as a guide.
# 
# You do NOT need to call the function main.

# ---- code start ----
from typing import Callable


def fahrenheit_to_celsius(temps_f: float) -> float:
    temps_c = (temps_f - 32) * 5 / 9
    return round(temps_c, 2)


def celsius_to_fahrenheit(temps_c: float) -> float:
    temps_f = temps_c * 9 / 5 + 32
    return round(temps_f, 2)


def select_converter_function_for_unit(unit: str) -> Callable[[float], float]:
    if unit == 'f':
        return fahrenheit_to_celsius
    else:
        return celsius_to_fahrenheit


def switch_unit(unit: str) -> str:
    if unit == 'f':
        return 'c'
    else:
        return 'f'


def print_temperature(temperature: float, unit: str):
    temperature = round(temperature, 1)
    print(" ".join([str(temperature), unit]))


def main():
    """Entry point of the program."""
    temperature, unit = input().split()  # read the input
    temperature = float(temperature)
    unit_converter = select_converter_function_for_unit(unit)
    temperature = unit_converter(temperature)
    unit = switch_unit(unit)
    print_temperature(temperature, unit)
