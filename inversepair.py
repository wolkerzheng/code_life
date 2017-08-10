# -*- coding:utf-8 -*-
"""
时间较大，超时
"""
class Solution:
    count = 0
    def InversePairs(self,data):
        print self.InversePairsHelp(data)
        return self.count
    def InversePairsHelp(self, data):
        # write code here
        if len(data) <= 1:
            return data
        l = len(data)/2
        left = self.InversePairsHelp(data[:l])
        right = self.InversePairsHelp(data[l:])
        sortnum = self.help(left,right)
        return sortnum

    def help(self,left,right):
        # i,j=0,0
        i,j = 0,0
        l1,l2 = len(left),len(right)
        nums = []
        while i<l1 and j<l2:
            if left[i]<=right[j]:
                nums.append(left[i])
                i +=1
            else:
                nums.append(right[j])
                self.count += l1-i
                if self.count>1000000007:
                    self.count %= 1000000007
                j += 1
        if i<l1:
            nums.extend(left[i:])
        if j<l2:
            nums.extend(right[j:])
        return nums

s =Solution()
data = [1,2,3,4,5,6,7,0]
print s.InversePairs(data)
# print divede([2,3,112,122,12,6])

