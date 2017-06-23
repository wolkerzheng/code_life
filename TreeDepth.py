# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import util
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if pRoot==None:
        	return 0
        return max(self.TreeDepth(pRoot.left),self.TreeDepth(pRoot.right) )+1
    
    def TreeDepth2(self, pRoot):
        # write code here
        """
	
        """
        if pRoot==None:
        	return 0
        d = 1
        queue = []
        queue.append(pRoot)
        last = pRoot
        while queue:     	
        	p = queue.pop(0)
        	# print p.val,d
        	if p.left:
        		queue.append(p.left)
        	if p.right:
        		queue.append(p.right)	
        	if last==p and queue:
        		last = queue[-1]
        		d +=1
        return d


 
n1 = [8,8,7,9,2,'#','#','#','#',4,7]
nums = [8,9,2]
root1 = util.BuildTree(n1,1)
root2 = util.BuildTree(nums,1)
s = Solution()
print s.TreeDepth2(root1)