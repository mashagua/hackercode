import os
import sys
def simpleArraySum(ar):
    #
    # Write your code here.
    total=0
    for i in range(len(ar)):
        total+=ar[i]
    return total

    #

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
