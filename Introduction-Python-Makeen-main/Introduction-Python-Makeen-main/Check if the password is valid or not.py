# -*- coding: utf-8 -*-
"""
Created on Sun May 14 22:28:06 2023

@author: HP
"""
length = lower = upper = digit = False


password = input('Enter the password: ')

if len(password) >= 8:
    length = True
    
    for i in password:
        if i.islower():
            lower = True
        elif i.isupper():
            upper = True
        elif i.isdigit():
            digit = True


if length and lower and upper and digit == True:
    print('That is a valid password.')
else:
    print('That password is not valid.')
