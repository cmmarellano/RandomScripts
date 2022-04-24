# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 12:01:25 2022

@author: Arellano
"""

import sys

#arg1 = sys.argv[1] + " " + sys.argv[2]
arg1 = sys.argv[1]
arg2 = sys.argv[2]



def hail_friend(args):
    print(f"Hail, {args}!")


def add_numbers(num1, num2):
    result_sum = int(arg1) + int(arg2)
    return result_sum


# Call function
#hail_friend(arg1)
add_numbers(arg1, arg2)
#print(type(arg1))
