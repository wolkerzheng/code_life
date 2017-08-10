# -*- coding:utf-8 -*-
import util
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        if pRoot is None:
        	return True
        return self.isSymetricalHelp(pRoot.left,pRoot.right)
        pass

    def isSymetricalHelp(self,root1,root2):
    	if root1 is None and root2 is None:
    		return True

    	elif root1 != None and root2 !=None:
    		if root1.val != root2.val:
    			return False
    		else:
    			return self.isSymetricalHelp(root1.left,root2.right) and self.isSymetricalHelp(root1.right,root2.left) 
    	else:
    		return False


n1 = [8,8,7,9,2,'#','#','#','#',4,7]
nums = [8,9,9]
root1 = util.BuildTree(n1,1)
root2 = util.BuildTree(nums,1)
s = Solution()
print s.isSymmetrical(root1)
print s.isSymmetrical(root2)