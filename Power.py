# -*- coding:utf-8 -*-
"""

第一种方法：使用递归，时间复杂度O(logn)   
      当n为偶数，a^n =（a^n/2）*（a^n/2）
      当n为奇数，a^n = a^[(n-1)/2] * a^[(n-1)/2] * a

  举例： 
      2^11 = 2^1 * 2^2 * 2^8
      2^1011 = 2^0001 * 2^0010 * 2^1000
  
  第二种方法：累乘，时间复杂度为O(n) 

"""
class Solution:
    def Power(self, base, exponent):
        # write code here
        res = 1
        for i in range(abs(exponent)):
        	res = res *base
        if exponent<0:
        	return 1/res
        return res

    def Power2(self, base, exponent):
        # write code here
        res = 1.0
        res  = self.help(base,abs(exponent))
        if exponent<0:
          return 1/res
        return res
    def help(self,base,n):
      """
      optimiste:  array instead of iterator
      """
      if n==1:
        return base
      if n==0:
        return 1
      if n%2==0:
        return self.help(base,n/2)*self.help(base,n/2)
      else:
        return self.help(base,(n-1)/2)*self.help(base,(n-1)/2)*base






s = Solution()
test = [1,2,3,-1]
for t in test:
    print s.Power(2.0,t)
    print s.Power2(2.0,t)