# -*- coding:utf-8 -*-
import util
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        
        if not pRootOfTree:
        	return pRootOfTree
        
        self.ConvertHelp(pRootOfTree)
        while pRootOfTree.left:
            pRootOfTree = pRootOfTree.left
        return pRootOfTree
    def ConvertHelp(self,root):

        if root.left:
            pre =  self.ConvertHelp(root.left)
            while pre.right:
                pre = pre.right
            pre.right = root
            root.left = pre
        if root.right:
            next = self.ConvertHelp(root.right)
            while next.left:
                next = next.left
            next.left = root
            root.right = next
        return root