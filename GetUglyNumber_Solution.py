# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index<7:
            return index
        res=[1]
        t2,t3,t5=0,0,0
        for i in xrange(1,index):
            res.append(min(res[t2]*2,res[t3]*3,res[t5]*5))
            # print t2,t3,t5
            # print res
            if res[-1] == res[t2]*2:
                t2+=1
            if res[-1] == res[t3]*3:
                t3+=1
            if res[-1] == res[t5]*5:
                t5+=1
        return res[index-1]


        pass


    def GetUglyNumber(self,N):
        res = 0
        for i in xrange(1,N+1):
            if self.isUglyNumber(i):
                res +=1
        return res


    def isUglyNumber(self,n):

        if n == 1:
            return True

        while n%2==0:
            n = n/2
        while n%3==0:
            n = n/3
        while n%5==0:
            n = n /5

        if n==1:
            return True
        else:
            return False


SS = Solution()
n = 7 #8
print SS.GetUglyNumber_Solution(7)