# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 00:33:14 2022

@author: Arellano
"""

import sys

# This code reads in arguments and converts those inputs to decimal numbers
first_number = float(sys.argv[1])
second_number = float(sys.argv[2])

# Your code goes here!
result_sum = first_number + second_number
result_difference = first_number - second_number
result_product = first_number*second_number
result_quotient = first_number/second_number


# labels
print(f"{first_number} plus {second_number} equals {result_sum}")
print(f"{first_number} minus {second_number} equals {result_difference}")
print(f"{first_number} multiplied by {second_number} equals {result_product}")
print(f"{first_number} divided by {second_number} equals {result_quotient}")