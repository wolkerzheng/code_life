# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        if s is None or s.strip()=='':
        	return s
        ss = s.split(' ')
        start,end = 0,len(ss)-1
        while start<end:
        	ss[start],ss[end] = ss[end],ss[start]
        	start+=1
        	end -=1
        return ' '.join(ss)


SS = Solution()

s = 'I am a student.'
print SS.ReverseSentence(s)
