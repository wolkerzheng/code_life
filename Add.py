# -*- coding:utf-8 -*-
class Solution:
    def Add(self, num1, num2):
        # write code here
        
        while num2!=0:
            tmp = num1^num2
            num2 = (num2&num1)<<1
            num1 = tmp
        return num1
    def addd2(self,n):
    	
    	return n and (n+self.addd2(n-1))
    	
    	

SS = Solution()
print SS.addd2(5)
print SS.Add(11,25)