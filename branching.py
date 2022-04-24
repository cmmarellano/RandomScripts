# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 17:24:32 2022
TwilioQuest: The Pythonic Temple
    Python Initiation: Conditional Logic 
    Trial of Branching Paths
@author: Arellano
"""

import sys

num_sum = (int(sys.argv[1]) + int(sys.argv[2]))


#test vars
# a = -1000
# b = 9
# num_sum = a + b
# print(f"a: {a}")
# print(f"b: {b}")


print(f"num_sum: {num_sum}")

if num_sum <= 0:
    print("You have chosen the path of destitution.")
if num_sum > 1 and num_sum<=100:
    print("You have chosen the path of plenty.")
if num_sum > 100:
    print("You have chosen the path of excess.")