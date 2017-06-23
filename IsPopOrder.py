# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if len(pushV) != len(popV):
            return False
        popIdx = 0
        pushIdx = 0
        stack = []
        stack.append(pushV[pushIdx])
        while pushIdx < len(pushV):
            while len(stack)>0 and  stack[-1] == popV[popIdx]:
                popIdx += 1
                stack.pop(-1)
            pushIdx += 1
            if pushIdx<len(pushV):
                stack.append(pushV[pushIdx])
        if stack == []:
            return True
        else:
            return False


s = Solution()
a = [1, 2, 3, 4, 5]
b = [1, 2, 4, 5,3]
print s.IsPopOrder(a, b)