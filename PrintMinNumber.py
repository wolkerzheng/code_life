# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if numbers==None or len(numbers)==0:
            return ""
        if len(numbers)==1:
            return numbers[0]
        n = map(str,numbers)
        queue = sorted(n,reverse=True)
        print queue
        while len(queue)>1:
            a,b = queue.pop(0),queue.pop(0)
            # print a,b
            queue.append(min(a+b,b+a))
            queue = sorted(queue)

        return queue[0]
        
    def PrintMinNumber2(self, numbers):

        if numbers is None:
            return ""
        lens = len(numbers)
        if lens==0:
            return ""
        tmpNumbers = sorted(numbers,cmp = self.compare)
        print tmpNumbers
        return int(''.join(str(x) for x in tmpNumbers))
    def compare(self,num1,num2):
        t = str(num1)+ str(num2)
        s = str(num2) + str(num1)
        if t>s:
            return 1
        elif t<s:
            return -1
        else:
            return 0
        

SS = Solution()
print sorted

numbers= [3,32,321] #321323
numbers = [3,323,32123] #"321233233"
numbers = [3334,3,3333332] #"333333233334"
numbers = [5,3,2,1,4]
# numbers= [3,32,321] #321323
print SS.PrintMinNumber(numbers)
print SS.PrintMinNumber2(numbers)