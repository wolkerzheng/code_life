# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        newHead  = ListNode(-1)
        p = pHead
        while p:
        	tmp = newHead.next
        	q = p.next
        	newHead.next = p
        	p.next = tmp
        	p = q
        return newHead.next 
        pass