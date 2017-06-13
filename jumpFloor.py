# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        
        if number<=2:
            return number
        dp = [0]*(number+1)
        dp[1]  =  1
        dp[2] = 2
        for i in range(3,number+1):

            dp[i] = dp[i-1] + dp[i-2]
        return dp[number]


s = Solution()
test = [0,1,2,3,4,5,6,7,8,9]
for n in test:
    print s.jumpFloor(n)