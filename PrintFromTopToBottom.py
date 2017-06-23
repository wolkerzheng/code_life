# -*- coding:utf-8 -*-
import util
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here

        if root == None:
        	return []
        res = []
        queue = []
        queue.append(root)
        while queue:
        	q = queue.pop(0)
        	if q.left:
        		queue.append(q.left)
        	if q.right:
        		queue.append(q.right)
        	res.append(q.val)
        return res