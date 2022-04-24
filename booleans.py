# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 14:22:47 2022
TwilioQuest: The Pythonic Temple
    Python Initiation: Booleans
@author: Arellano
"""



# Give arguments
import sys
arg1 = sys.argv[1]

# Boolean variables declaration
python_is_glorious = True
failure_is_option = False


print(f"python_is_glorious: {python_is_glorious}")
print(f"failure_is_option: {failure_is_option}")
proper_greeting = False #initialize
if arg1 == "For the glory of Python!":
    proper_greeting = True
    print(f"proper_greeting : {proper_greeting} ")
else:
    proper_greeting = False
    print(f"proper_greeting : {proper_greeting} ")