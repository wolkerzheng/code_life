# -*- coding:utf-8 -*-
import util
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here

        if pRoot is None:
        	return []
        queue = []
        queue.append(pRoot)
        res = []
        last = pRoot
        tmp = []
        row=0
        while queue:
        	p = queue.pop(0)
        	tmp.append(p)
        	if p.left:
        		queue.append(p.left)
        	if p.right:
        		queue.append(p.right)
        	if p == last:
        		if queue:
        			last = queue[-1]
        		if row%2==1:
        			tmp.reverse()
        		res.append(tmp)
        		row+=1
        		tmp = []
        return res

n1 = [8,8,7,9,2,'#','#','#','#',4,7]
nums = [8,9,2]
root1 = util.BuildTree(n1,1)
root2 = util.BuildTree(nums,1)
s = Solution()
print s.Print(root1)
print s.Print(root2)
        		
