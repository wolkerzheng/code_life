# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if head ==None or k == 0:
        	return head
        p = head
        while k>0:
        	k-=1
        	p=p.next
        if k!=0 :
            return p
        res= head
        while p:
        	p = p.next
        	res= res.next
        return res