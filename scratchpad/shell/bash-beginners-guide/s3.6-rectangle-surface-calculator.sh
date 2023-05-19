#!/usr/bin/env bash

# 3.6-rectangle-surface-calculator.sh
# This script takes reads two arguments which are the sides of a rectangle
# and prints out the circumference of the rectangle that has these proportions.

# Print a greeting message that will explain the purpose of this script.
echo $'Hello, this is a script to calculate the surface area of a rectangle 
from it\'s sides, you will be asked to input the sides and will be presented 
with the surface area'

# Read the first side.
echo 'Please enter the first side of the rectangle'
read SIDE1
echo 'Now please enter the second side of the rectangle'
read SIDE2
echo 'The surface area of the rectangle is: ' $((2*(SIDE2+SIDE1)))


