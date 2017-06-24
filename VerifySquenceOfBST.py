# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if sequence == None or len(sequence)<=0:
        	return True
        root = sequence[-1]
        # print sequence
        i = 0
        while i<len(sequence)-1:
        	if sequence[i]>root:
        		break
        	i +=1
        # print i
        for j in range(i,len(sequence)):
        	if sequence[j] < root:
        		return False
        return self.VerifySquenceOfBST(sequence[:i]) and self.VerifySquenceOfBST( sequence[i:-1])
        


s  = Solution()
# n = [7,4,6,5]
n = [5,7,6,9,11,10,8]
print s.VerifySquenceOfBST(n)