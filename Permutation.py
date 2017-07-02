# -*- coding:utf-8 -*-
import itertools
class Solution:
    def Permutation(self, ss):
        # write code here
        """
        
        """
        
        res =[]
        if ss == '':
        	return res
        lst = list(itertools.permutations(list(ss),len(ss)))
        for i in range(len(lst)):
              lst[i] = ''.join(lst[i])
        l = list(set(lst))
        return (sorted(l))

        def Permutation(self, ss):
	        # write code here
	        """
	        
	        """
	        res =[]
	        if ss == '':
	        	return res
	        lst = list(itertools.permutations(list(ss),len(ss)))
	        for i in range(len(lst)):
	              lst[i] = ''.join(lst[i])
	        l = list(set(lst))
	        return (sorted(l))
    # def Permuta(self, begin,slist): 	
    # 	if len(slist)==1:
    # 		return begin + slist
    # 	tmp = []
    # 	for i in range(len(slist)):
    # 		tmp.append(begin + self.Permuta(,))
    # 	return tmp


s=Solution()

print s.Permutation('abc')
