# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if rotateArray==None or len(rotateArray)==0:
        	return 0
        start,end = 0,len(rotateArray)-1
        # mid = (start + end) / 2
        while start<end:
        	mid = (start + end) / 2
        	if mid+1< len(rotateArray) and rotateArray[mid]>rotateArray[mid+1]:
        		return rotateArray[mid+1]
        	elif mid< len(rotateArray) and rotateArray[mid]<rotateArray[end]:
        		end = mid
        	else:
        		start = mid
        return rotateArray[mid]
s = Solution()
print s.minNumberInRotateArray([3,4,5,1,2])