import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
total_swap=0
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            total_swap+=1
            a[i],a[j]=a[j],a[i]
print("Array is sorted in "+str(total_swap)+" swaps.")
print("First Element: "+str(a[0]))
print("Last Element: "+str(a[-1]))