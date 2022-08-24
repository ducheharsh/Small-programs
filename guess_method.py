# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
 
cube = int(input("Enter a number"))
guess = 0
ep = 0.001
incr = 1
while  abs(guess**3 - cube) >= ep:
    guess += incr
print(guess , "is the closest one")
        
    
