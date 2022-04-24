# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 00:49:07 2022

@author: Arellano
"""


import sys

# Create list
order_of_succession = sys.argv


print("Leaders:")
for index, item in enumerate(order_of_succession, start=1):
    str_print = f"{index}. {item}"
    print(str_print)
    
    
    
order_of_succession.pop(0)