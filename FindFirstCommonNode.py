# -*- coding:utf-8 -*-
class ListNode:
     def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def getLen(self,pHead):
        res=  0
        if pHead==None:
            return res
        
        while pHead:
            res += 1
            pHead = pHead.next
        return res
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        l1 = self.getLen(pHead1)
        l2 = self.getLen(pHead2)
        if l1>l2:
            k = l1-l2
            l= 0
            while l<k and pHead1:
                pHead1 = pHead1.next
                l+=1
                
        if l2>l1:
            k = l2-l1
            l=0
            while l<k and pHead2:
                pHead2 = pHead2.next
                l+=1
                
        while pHead1 and pHead2:
            if pHead2==pHead1:
                return pHead1
            pHead1 = pHead1.next
            pHead2 = pHead2.next
        return None