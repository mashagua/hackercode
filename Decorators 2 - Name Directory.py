# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 09:21:53 2019

@author: masha
"""

import operator

def person_lister(f):
    def inner(people):
        # return map(f,sorted(people, key=operator.itemgetter(2)))
        return map(f,sorted(people, key=lambda x: int(x[2])))
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')
    
"""
3
Mike Thomson 20 M
Robert Bustle 32 M
Andria Bustle 30 F
"""