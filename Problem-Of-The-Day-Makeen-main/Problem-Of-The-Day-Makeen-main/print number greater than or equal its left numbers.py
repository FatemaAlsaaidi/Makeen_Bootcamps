# -*- coding: utf-8 -*-
"""
Created on Sun May 28 19:56:59 2023

@author: HP
"""

y= input("Enter list of number: ")

for i in range(len(y)):
    x=y.split(" ")
print(x)

for i in range(len(x)-1,0,-1):
    j = i-1
    if i>=j:
        print(x[i], end=" ")
    if max(x) == x[i]:
        break