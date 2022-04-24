# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 16:00:46 2022
TwilioQuest: The Pythonic Temple
    Python Initiation: Create Python class
@author: Arellano
"""


# import sys


#Creating Python class to describe a citizen of Python
class Citizen:
    """
    Class that describes a citizen.
    Requires first name and last name.
    Returns full name
    
    """
    
    # init method
    def __init__(self, first_name, last_name):
        #argument to instance variables
        self.first_name = first_name  
        self.last_name = last_name
        
     #instance method  
    def full_name(self):
        return (self.first_name + " " + self.last_name)
    
        
    # class variable 
    greeting = "For the glory of Python!"


# Execute class and  call arguments
#x = Citizen(sys.argv[1], sys.argv[2])   #if sys argument will be given
# x = Citizen("Satoru", "Gojo")          # if given str
# print(x.greeting)
# print(f"first name: {x.first_name}")
# print(f"last name: {x.last_name}")
# print(x.full_name("Satoru", "Gojo"))



