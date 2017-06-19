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
        result = False
        if pRoot1 and pRoot2:
        	if pRoot1.val == pRoot2.val:
        		result = self.DoesTree1haveTree2(pRoot1,pRoot2)
        	if not result:
        		result = self.HasSubtree(pRoot1.left,pRoot2)
        	if not result:
        		result = self.HasSubtree(pRoot1.right,pRoot2)

        return result
    def DoesTree1haveTree2(self,pRoot1,pRoot2):

     	if not pRoot2:
     		return True
     	if not pRoot1:
     		return False
     	if pRoot1.val!=pRoot2.val:
     		return False
     	return self.DoesTree1haveTree2(pRoot1.left,pRoot2.left) and self.DoesTree1haveTree2(pRoot1.right,pRoot2.right)

n1 = [8,8,7,9,2,'#','#','#','#',4,7]
nums = [8,9,2]
root1 = util.BuildTree(n1,1)
root2 = util.BuildTree(nums,1)
s = Solution()
print s.HasSubtree(root1,root2)




