#-*- coding:utf-8 -*-
import util

class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if root == None:
        	return None
        tmpleft = root.left
        root.left = self.Mirror(root.right)
        root.right =  self.Mirror(tmpleft)
        return root

n1 = [8,8,7,9,2,'#','#','#','#',4,7]
nums = [8,9,2]
root1 = util.BuildTree(n1,1)
root2 = util.BuildTree(nums,1)
s = Solution()
print util.bfs(s.Mirror(root1))
print util.bfs(s.Mirror(root2))
