# -*- coding: utf-8 -*-
"""
Created on Tue May 16 07:07:50 2023

@author: HP
"""

x=input("please enter your numbers list:")
x.split(",")
count_dict={}
for i in x:
    if i in count_dict:
        count_dict[i]+=1
    else:
        count_dict[i]=1
for key,value in count_dict.items():
    if value ==1:
        print(key)
        break