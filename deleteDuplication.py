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
        p = pHead.next
        while last.next:

        	if last.val == p.val:
        		p = p.next
        		while p.next  and last.val == p.val:
        			p = p.next
	        	last.next = p
	        else:
	        	last = last.next
	        	p = p.next

        return tmpHead.next