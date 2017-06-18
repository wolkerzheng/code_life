# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here

        if array==None or len(array)<=1:
        	return array
        s,e = 0,len(array)-1

        while s<e:

        	while s<e and array[s]%2==1:
        		s+=1
        	while s<e and array[e]%2==0:
        		e-=1
        	if s<e:
        		array[s],array[e] = array[e],array[s]
        return array
    def reOrderArray2(self, array):
        # write code here

        if array==None or len(array)<=1:
            return array

        s,e = 0,len(array)-1
        copyarray = [0]*len(array)
        count = 0
        for i in xrange(len(array)):
            if  array[i] %2 == 1:
                count +=1

        for i in xrange(len(array)):
            if  array[i] %2 == 1:
                copyarray[s] = array[i]
                s+=1
            else:
                copyarray[count] = array[i]
                count +=1
        for i in xrange(len(array)):
                array[i] = copyarray[i]
        return array
s = Solution()
num = [1,2,3,4,5]
print s.reOrderArray(num) 
num = [1,2,3,4,5]
print s.reOrderArray2(num)     