# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if numbers==None or len(numbers)==0:
            return -1
        if len(numbers)==1:
            return numbers[0]
        n = map(str,numbers)
        queue = sorted(n,reverse=True)
        print queue
        while len(queue)>1:

            a,b = queue.pop(0),queue.pop(0)

            queue.append(min(a+b,b+a))
            queue = sorted(queue,reverse=True)
        return queue[0]
        


SS = Solution()
print sorted
numbers= [3,32,321] #321323
numbers = [3,323,32123] #"321233233"
numbers = [3334,3,3333332] #"333333233334"
print SS.PrintMinNumber(numbers)