# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here

        res = []
        if len(array)<=0:
            return []
        s,e = 0,len(array)-1

        while s<e:
            if array[s]+array[e]==tsum:
                res.append(array[s])
                res.append(array[e])
                break
            elif array[s]+array[e]<tsum:
                s += 1
            else:
                e -= 1
        # if res==[]:
        #     return []
        # minNum = res[0][0]*res[0][1]
        # result1,result2 = res[0][0],res[0][1]
        # for n1,n2 in res:
        #     if n1*n2<minNum:
        #         result1,result2 = n1,n2
        return res

SS = Solution()

print SS.FindNumbersWithSum()