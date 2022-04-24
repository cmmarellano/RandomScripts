# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 18:14:28 2022
TwilioQuest: The Pythonic Temple
    Python Initiation: Fizzbuzz
    Trial of Trickery
@author: Arellano
"""
import sys

# Take arguments from command line
args = sys.argv
args.pop(0)


#test print of arguments
#print(f"arguments given:  {args}")

#Convert list values into int
args = list(map(int, args))
#print(f"args[0] :  {args[0]}")

#Loop
for num in args:
    if num % 3 == 0 and num % 5 ==0:
            print("fizzbuzz")
    elif num % 3 == 0:
        print("fizz")
    elif num % 5 ==0:
        print("buzz")
    else:
        print(num)