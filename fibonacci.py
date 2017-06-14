# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n<=1:
        	return n
        f = [0]*n
        f[0] = 1
        f[1] = 1
        for i in xrange(2,n):
        	f[i] = f[i-1]+f[i-2]
        return f[n-1]
        pass

s = Solution()

test = [0,1,2,3,4,5]
for i in test:
	print s.Fibonacci(i)