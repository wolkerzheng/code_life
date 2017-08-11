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
        
        stack = []
        idx = 1
        while pRoot or stack:
            
            while pRoot:
                stack.append(pRoot)
                pRoot = pRoot.left
            pRoot = stack.pop(-1)
            if idx == k:
                return pRoot
            idx += 1
            pRoot = pRoot.right 
        return None

        # print res


n1 = [8,8,7,9,2,'#','#','#','#',4,7]
nums = [8,2,9]
root1 = util.BuildTree(n1,1)
root2 = util.BuildTree(nums,1)
s = Solution()
print s.KthNode(root1,3)
print s.KthNode(root2,1)