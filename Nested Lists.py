# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 07:39:45 2019
Email：Shaoguang.MA@cn.bosch.com
@author: MSA2SGH

Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

"""

marksheet=[]
scorelist=[]

for _ in range(int(input())):
    name = input()
    score = float(input())
    marksheet+=[[name,score]]
    scorelist+=[score]

scorelist = list(dict.fromkeys(scorelist))
b=sorted(scorelist)[1] 

for a,c in sorted(marksheet):
    if c==b:
        print(a)
#不通过
if __name__ == '__main__':
    list_all=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list_all.append([name,score])
    list_all.sort(key=lambda x: x[1])
    score=[ele[1] for ele in list_all]
    unique_score=set(score)
    target_score=sorted(unique_score)[1]
    sel_person=[ele[0] for ele in list_all if ele[1]==target_score]
    for i in range(len(list_all)):
        if list_all[i][1]==target_score:
            print(list_all[i][0])
    
        
