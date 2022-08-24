#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 00:44:41 2022

@author: harsh
"""

cube = 1000
low = 0
ep = 0.00001
high = cube
guess = (high + low )/2.0
while abs(guess**3 - cube) >= ep:
    if guess**3 < cube:
        low = guess
    else:
        high = guess
    guess = (high + low)/2.0
print(guess , "is the cube root")
    