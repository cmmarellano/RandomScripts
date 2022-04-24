# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 11:54:09 2022
TwilioQuest: The Pythonic Temple
Python Initiation: List Iteration
@author: Arellano
"""


import sys

# Create list
order_of_succession = sys.argv
# pass on the first sys.argv
order_of_succession.pop(0)


# For loop for every item, together with their index 
print("Leaders:")
for index, item in enumerate(order_of_succession, start=1):
    str_print = f"{index}. {item}"
    print(str_print)
    
    
