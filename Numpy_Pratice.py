# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 22:14:12 2018

@author: Anjali Brajendra
"""

import numpy as np

""" Create a 3x3 matrix"""
'''
matrix1 = np.arange(1,10).reshape(3,3)
matrix2 = np.arange(1,10).reshape(3,3)
print(matrix1)
print("------------------------")
print(matrix2)
print("---------Result---------------")
print(matrix1 + matrix2)'''
"""End """

vector = np.zeros(10)
vector[6]=11
print(vector)

"""Write a Python program to reverse an array (first element becomes last)"""
arr = np.arange(12,38)
print(arr)
print(arr[::-1])

print(np.asfarray(arr))
print(np.ones((5,5)))

a = np.array(['4','2','3'])
np.copyto(b,a)
print(b)
