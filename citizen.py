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
    
    """
    
    
    # class variable 
    greeting = "For the glory of Python!"
    
    # init method
    def __init__(self, first_name, last_name):
        #argument to instance variables
        self.first = first_name  
        self.last = last_name
        
     #instance method  
    def full_name(self):
        self.name = self.first + " " + self.last
        print(self.name)
        return (self.name)


# Execute class and  call arguments
#x = Citizen(sys.argv[1], sys.argv[2])   #if  argument will be given

Citizen("Satoru", "Gojo")
print(Citizen.greeting)
Citizen.full_name()

