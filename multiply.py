# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        aLen = len(A)
        B = [1]*len(A)

        if aLen!=0:
        	B[0] =1
        	for i in range(1,aLen):
        		B[i] = B[i-1]*A[i-1]
        	tmp = 1
        	for j in range(aLen-2,-1,-1):
        		tmp*=A[j+1]
        		B[j] *= tmp
        return B

SS = Solution()

A = []

print SS.multiply(A)