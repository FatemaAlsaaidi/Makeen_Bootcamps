# -*- coding: utf-8 -*-
"""
Created on Tue May  9 19:30:20 2023

@author: HP
"""
import numpy as np
import math as m
s1=[-10,20,-10,-18]
s2=[-10,20,0,3]
s3=[0,3,8,17]
s4=[8,17,10,-16]
s5=[10,-16,-10,-18]

matrix=[s1,s2,s3,s4,s5]
a=np.array(matrix)

length=[]
slop=[]
max_y=[]
min_y=[]
for i in range(5):
        s=(a[i][3]-a[i][1])/(a[i][2]-a[i][0])
        max_y.append(a[i][1])
        max_y.append(a[i][3])
        l=m.sqrt((a[i][3]-a[i][1])**2 +(a[i][2]-a[i][0])**2)
        length.append(round(l,2))
        min_y.append(a[i][1])
        min_y.append(a[i][3])
        slop.append(s)
        
print("The lengths of vectors are",length)   
print("The slops of vectors are ",slop)
print("The max of y axis is", max(max_y))
print("The min of y axis is",min(min_y))







