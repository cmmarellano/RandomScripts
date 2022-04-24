# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 14:22:47 2022
TwilioQuest: The Pythonic Temple
    Python Initiation: Booleans
@author: Arellano
"""


# Boolean variables declaration
python_is_glorious = True
failure_is_option = False

# Give arguments
import sys
arg1 = sys.argv


if arg1 == "For the glory of Python!":
    proper_greeting = True
    print(proper_greeting)
else:
    proper_greeting = False
    print(proper_greeting)