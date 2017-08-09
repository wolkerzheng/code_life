# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        if numbers is None or len(numbers)<=0:
        	return False
        for n in numbers:
        	if n<0 or n>=len(numbers):
        		return False
        idx = 0
        # for i in range(len(numbers)):

        #     while i != numbers[i]:
        #         # break
        #         if numbers[i] == numbers[numbers[i]]:
        #             duplication[0] = numbers[i]
        #             return True
        #         else:
        #             tmp = numbers[i]
        #             numbers[i]= numbers[numbers[i]]
        #             numbers[tmp] = tmp
                # print numbers
        while idx<len(numbers):
        	if numbers[idx] == idx:
        		idx += 1
        	else:
        		if numbers[idx] == numbers[numbers[idx]]:
        				duplication[0] = numbers[idx]
        				return True
        		# print numbers[idx],numbers[numbers[idx]]
        		tmp = numbers[idx]
        		numbers[idx]= numbers[numbers[idx]]
        		numbers[tmp] = tmp
        # 	print numbers
        return False


S = Solution()
n = [2,3,1,0,2,5,3]
dup = [0]
print S.duplicate(n,dup),dup[0]