# -*- coding: utf-8 -*-
"""
Created on Wed May 10 22:44:21 2023

@author: HP
"""

x=input("Enter degree")
len_x=len(x)
last_len_x=x[-1]

if last_len_x=="C":
    r1=(float(x[:-1])*9/5)+32
    print(r1)
elif last_len_x=="F":
    r2=((float(x[:-1])-32)*5)/9
    print(r2)
else:
    print("Ther is an error")
