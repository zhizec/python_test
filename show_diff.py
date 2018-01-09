# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 18:03:53 2018

@author: zhizec
"""

f = open("2018_1_7_1755.diff","r")  
lines = f.readlines()
count = 0
for line in lines:
    if line[0] is '+':
        count += 1
print(count)