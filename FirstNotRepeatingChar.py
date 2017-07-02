# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if s==None or len(s)==0:
            return -1
        chardict = {}
        for c in s:
            chardict[c] = chardict.get(c,0) + 1
        for i in range(len(s)):
            if chardict[s[i]] == 1:
                break
        return i


s = Solution()
ss = 'google'
print s.FirstNotRepeatingChar(ss)