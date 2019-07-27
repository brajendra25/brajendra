# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 20:30:23 2018

@author: Anjali Brajendra
"""

"""
Area of Circle"
"""
"""
pi = 3.14
radious = int(input("Enter Radious for Circle : "))
area_cir = (pi * (radious*radious));
print("Area or Circle : ", area_cir)
"""
"""
Write a Python program which accepts a sequence of comma-separated numbers 
from user and generate a list and a tuple with those numbers
"""
n = int(input("Eneter a value:- "))
result = (n * (n + 1))/2
print(result)


"""Fibonacci numbers"""
f_result = []
out_arr=[]
for x in range(n):
    f_result.append(x)
    
print(f_result)
index = 0;
for y in f_result:
    if index < len(f_result)-1:
        out_arr.append(f_result[index] + f_result[index+1])
        index=index+1;
print(out_arr)