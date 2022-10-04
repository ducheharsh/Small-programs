# -*- coding: utf-8 -*-
 
# This is small python program to find cube root using Guess method
  
cube = int(input("Enter a number: "))
guess = 0
ep = 0.001
incr = 1
while abs(guess**3 - cube) >= ep and guess <= cube: 
    guess += incr
if abs(guess**3 - cube) >= ep:
    print("Not a perfect cube")
else:
    print (guess , "is the cube root of" , cube)
    
