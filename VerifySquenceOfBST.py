# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if sequence==[]:
        	return False
        return self.help(sequence)
    def help(self,sequence):
	if len(sequence)<=1:
		return True
	root = sequence[-1]
	# print sequence
	i = 0
	while i<len(sequence)-1:
		if sequence[i]>root:
			break
		i +=1
	for j in range(i,len(sequence)-1):
		if sequence[j] < root:
			return False
	# print sequence[:i], sequence[i:-1]
	return self.help(sequence[:i]) and self.help( sequence[i:-1])


       

s  = Solution()
# n = [7,4,6,5]	#Flase
# n = [4,6,7,5]	#True
# n = [5,7,6,9,11,10,8] #True
print s.VerifySquenceOfBST( n)