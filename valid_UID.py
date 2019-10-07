# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 18:02:44 2019

@author: masha
"""

x= [input() for i in range(int(input()))]
for i in range(len(x)):
    if len(set(list(x[i])))==len(list(x[i])):
        print('Valid')
    else:
        print('Invalid')

