# -*- coding:utf-8 -*-
"""
前序遍历序列{1,2,4,7,3,5,6,8}
和中序遍历序列{4,7,2,1,5,3,8,6}
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre) == 0:
        	return None
        val  = pre[0]
        root = TreeNode(val)
        idx = tin.index(val)
        leftlen,rightlen = 0,0
        for  i in tin:
         	if i != idx:
         		leftlen += 1


        rightlen = len(tin) - leftlen-1 
        root.left = self.reConstructBinaryTree(pre[1:1+leftlen],tin[0:idx-1])
        root.right = self.reConstructBinaryTree(pre[1+leftlen:],tin[idx:idx+rightlen])

        pass
pre = [1,2,4,7,3,5,6,8]
tin = [4,7,2,1,5,3,8,6]
s = Solution()
s.reConstructBinaryTree(pre, tin)