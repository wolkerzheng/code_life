# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here

        if pRoot is None:
        	return []

        tmp,res,queue =[],[],[]
        queue.append(pRoot)
        last = queue[-1]
        while queue:
        	p = queue.pop(0)
        	tmp.append(p.val)
        	if p.left:
        		queue.append(p.left)
        	if p.right:
        		queue.append(p.right)
        	if last== p:
        		res.append(tmp)
        		if queue:
        			last = queue[-1]
        		tmp = []
        return res

SS = Solution()
