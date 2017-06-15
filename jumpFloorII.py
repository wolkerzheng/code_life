# -*- coding:utf-8 -*-
"""
1:1
2:2
3:4
4:8
5:16
f[1] = 1
f[2] = f[1]+f[2]
f[n-1] =f[n-1-1]+f[n-1-2]+.....+f[1]
f[n] = f[n-1] + f[n-2] + f[n-3] + ... + f[1]
f[n] = f[n-1] + f[n-1] = 2*f[n-1]
"""
class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number <=2:
            return number
        f = [0]*(number+1)
        f[1] = 1
        f[2] = 2 
        for i in xrange(2,number+1):
            f[i] = 2*f[i-1]
        return f[number]

if __name__ == '__main__':
    s = Solution()
    print s.jumpFloorII(3)