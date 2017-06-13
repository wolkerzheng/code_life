# -*- coding:utf-8 -*-
class Solution:
    stack1,stack2 = [],[]
    def push(self, node):
        # write code here
    	self.stack1.append(node)
    def pop(self):
        # return xx
        if self.stack2==[] and self.stack1==[]:
        	return -1
        if self.stack2 == []:
        	while self.stack1!=[]:
        		self.stack2.append(self.stack1.pop(-1))
 	     
        return self.stack2.pop(-1)

