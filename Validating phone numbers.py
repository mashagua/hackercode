import re
x= [input() for i in range(int(input()))]
for i in range(len(x)):
    aa=re.match(r'[789]\d{9}$',x[i])
    if aa:
        print('Yes')
    else:
        print('No')

