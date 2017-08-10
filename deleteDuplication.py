# -*- coding:utf-8 -*-
import util
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here

        if pHead is None or pHead.next is None:
        	return pHead
        tmpHead = ListNode(-1)
        tmpHead.next = pHead
        last = tmpHead
        p = pHead
        while p and p.next:
        	if p.next.val == p.val:
        		val = p.val
        		while p and p.val == val:
        			p = p.next
        		last.next = p
	        else:
	        	last = p
	        	p = p.next
        return tmpHead.next

SS =Solution()
t = SS.deleteDuplication(util.BuildListNode([1,1,2,3,3,3,4,4,5]))
print util.printListNode(t)