# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 00:51:16 2018

@author: Anjali Brajendra
"""

import cv2
img = cv2.imread("lab1.png")
y=0
x=0
h=180
w=200
while True:
    crop_img = img[y:y+h, x:x+w]
    cv2.imshow("cropped", crop_img)
    cv2.waitKey(0)
    print(x,y)
    y = h + y
    x = w + x
    key = cv2.waitKey(1) & 0xFF
    print(key)
    if key == ord("x"):
        break

