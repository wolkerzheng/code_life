# -*- coding:utf-8 -*-
import util
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if not pRoot1 and not pRoot2:
        	return True
        elif pRoot1 and pRoot2:
        	if pRoot1.val != pRoot2.val:
        		return False or  self.HasSubtree(pRoot1.left,pRoot2) or  self.HasSubtree(pRoot1.right,pRoot2) 
        	else:
        		return (self.HasSubtree(pRoot1.left,pRoot2.left) and self.HasSubtree(pRoot1.right,pRoot2.right))
        else:
        	return True


n1 = [8,8,7,9,2,'#','#','#','#',4,7]
nums = [8,9,1]
root1 = util.BuildTree(n1,1)
root2 = util.BuildTree(nums,1)
s = Solution()
print s.HasSubtree(root1,root2)




