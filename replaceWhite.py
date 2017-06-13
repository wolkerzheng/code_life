# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        	# write code here
	if s == None:
		return        
	numWhite = 0
	n = len(s)        
	for i in s:
	    if i==' ':
	        numWhite += 1
	newN = n + numWhite * 2
	resStr = ""
	for i in range(n-1,-1,-1):
		if  s[i]!=' ':
			resStr  = s[i]+resStr
		else:
			resStr = '%20'+resStr
	return resStr

if __name__ == '__main__':
	s = Solution()
	print s.replaceSpace('hello world')