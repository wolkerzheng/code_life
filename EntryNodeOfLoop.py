# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here 
        meetingnode = self.meetNode(pHead)
        if meetingnode is None:
        	return None
        nodeNum = 1
        p = meetingnode
        while p.next!=meetingnode:

        	p = p.next
        	nodeNum += 1
        p = pHead
        for i in range(nodeNum):
        	p = p.next

        q = pHead
        while p!=q:
        	p = p.next
        	q = q.next
        return p



    def meetNode(self,pHead):

    	if not pHead:
    		return None
    	slow = pHead.next
    	if not slow:
    		return None
    	fast = slow.next
    	while fast and slow:
    		if fast == slow:
    			return fast
    		slow = slow.next

    		fast =  fast.next
    		if fast:
    			fast = fast.next
    	return None


