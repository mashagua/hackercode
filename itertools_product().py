# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 09:48:35 2019
Email：Shaoguang.MA@cn.bosch.com
@author: MSA2SGH
"""

from itertools import product
A=input().split(' ')
B=input().split(" ")
A=[int(ele) for ele in A]
B=[int(ele) for ele in B]
print(*product(A, B))
