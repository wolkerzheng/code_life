# -*- coding:utf-8 -*-
"""
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
"""
class Solution:
    def NumberOf1(self, n):
        # write code here
        count = 0
        while n != 0:
        	 n = n&(n-1)
        	 count += 1
        return count 

s = Solution()
test = [1,2,3,-10]
for t in test:
	print s.NumberOf1(t)