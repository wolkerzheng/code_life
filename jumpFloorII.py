# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number <=2:
            return number
        f = [0]*(number+1)
        f[1] = 1
        f[2] = 2
        for i in xrange(2,number+1):
            

if __name__ == '__main__':
    s = Solution()
    print s.jumpFloorII(3)