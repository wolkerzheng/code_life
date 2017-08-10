# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import util
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        if pRoot is None or k<=0:
        	return None
        res= []
        stack = [pRoot]

        while stack:
            
            p = stack[-1]
            if p.right:
                stack.append(p.right)
            if p.left:
                stack.append(p.left)
            if not p.left and not p.right:
                
        print res


n1 = [8,8,7,9,2,'#','#','#','#',4,7]
nums = [8,9,2]
root1 = util.BuildTree(n1,1)
root2 = util.BuildTree(nums,1)
s = Solution()
print s.KthNode(root1,3)
print s.KthNode(root2,1)