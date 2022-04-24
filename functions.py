# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 12:01:25 2022
TwilioQuest: The Pythonic Temple
Python Intiation: Functions I and II

@author: Arellano
"""

#import sys

# Functions.py part1 vars
#arg1 = sys.argv[1] + " " + sys.argv[2]
#arg1 = sys.argv[1]
#arg2 = sys.argv[2]

# Functions.py part2 vars
num1 = 1
num2 = 5


def hail_friend(args):
    print(f"Hail, {args}!")


def add_numbers(num1, num2):
    result_sum = int(num1) + int(num2)
    return result_sum


# Call functions

#hail_friend(arg1)

print(f"first_number: {num1} ")
print(f"second_number: {num2} ")
print(add_numbers(num1, num2))
#print(type(arg1))
