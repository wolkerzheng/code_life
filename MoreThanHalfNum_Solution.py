# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if numbers == None or len(numbers)==0:
        	return 0
        count =1 
        num = numbers[0]
        for i in range(1,len(numbers)):
        	if num==numbers[i]:
        		count += 1
        	else:
        		count -= 1
        		if count == 0:
        			count = 1
        			num = numbers[i]
        	print count
        count =0
        for i in range(len(numbers)):
        	if numbers[i] == num:
        		count += 1

        if count >= len(numbers)/2:
        	return num
        else:
        	return 0

s = Solution()
n = [2,2,2,2,2,1,3,4,5]
print s.MoreThanHalfNum_Solution(n)