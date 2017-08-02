# -*- coding:utf-8 -*-
class Solution:
    ##利用数学公式，(首项+尾项）*项数 /2
    def FindContinuousSequence(self, tsum):
        # write code here
        res = []
        sum = 0
        stack = []
        end = (tsum+1)/2+1
        for i in range(1,end):
            # print stack
            stack.append(i)
            sum += i
            while sum>tsum and stack!=[]:
                sum -= stack.pop(0)
                # print sum
            if sum == tsum:
                # print 'stack',stack
                res.append([x for x in stack])
                sum = sum - stack.pop(0)
        # print resList
        return res

ss = Solution()
tsum = 3
print ss.FindContinuousSequence(tsum)