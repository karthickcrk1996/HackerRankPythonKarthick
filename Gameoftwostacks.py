#!/bin/python3

import os
import sys

#
# Complete the twoStacks function below.
#
def twoStacks(x, a, b):
    n=len(a)
    m=len(b)
    i, j, sum = 0,0,0
    while i<n and (sum+a[i])<=x:
        sum+=a[i]
        i+=1
    ans=i
    while j<m and i>=0:
        sum+=b[j]
        j+=1
        while sum>x and i>0:
            i-=1
            sum-=a[i]
        if sum<=x and i+j>ans:
            ans=i+j
    return ans
   
            
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        nmx = input().split()

        n = int(nmx[0])

        m = int(nmx[1])

        x = int(nmx[2])

        a = list(map(int, input().rstrip().split()))

        b = list(map(int, input().rstrip().split()))

        result = twoStacks(x, a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
