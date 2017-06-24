# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        head = RandomListNode(-1)
        p  = head
        while pHead:
        	tmp = RandomListNode(-1)
        	tmp.val = pHead.val
        	tmp.random = pHead.random
        	p.next = tmp
        	p = p.next
        	pHead = pHead.next 
        return head.next
        pass

