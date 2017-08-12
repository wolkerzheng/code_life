# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        if len(num)<size:
        	return []
        if size == 0:
        	return num
        res = []
        queue = []
        for i in range(size):
        	queue.append(num[i])
        res.append(max(queue))
        for i in range(size,len(num)):
        	queue.pop(0)
        	queue.append(num[i])
        	res.append(max(queue))
        return res

SS = Solution()

num = [2,3,4,2,6,2,5,1]
size = 3

print SS.maxInWindows(num,size)