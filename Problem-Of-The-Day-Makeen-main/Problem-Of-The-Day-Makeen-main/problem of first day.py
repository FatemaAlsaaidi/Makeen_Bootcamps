# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
"""  Problem of  first day  """
""" Write program that compare 3 numbers and give the biggest number or 
tell user if the numbers are equal """
n1 = int(input("n1="))
n2 = int(input("n2="))
n3 = int(input("n3="))

num =[n1, n2, n3]
if num[0]==num[1]==num[2]:
    print("The numbers are equals")
else:
    print("The biggest number is " + max(num))
