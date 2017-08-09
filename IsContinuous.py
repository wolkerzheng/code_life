# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if len(numbers)<=0:
            return False
        num = sorted(numbers)
        
        zero = 0
        gap = 0
        for i in range(2):
            if num[i] == 0:
                zero += 1
        last = zero
        # print last,zero
        for i in range(zero+1,len(num)):
            # print num[i],num[last]
            if num[last]==num[i]:
                return False
            else:
                gap += num[i]-num[last]-1
                last = i
        print gap
        if gap>zero:
            return False
        else:
            return True


SS= Solution()
numbers=[0,0,3,4,5]
print SS.IsContinuous(numbers)