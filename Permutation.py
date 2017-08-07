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

    def Permutation2(self, ss):
        # write code here
        """
        
        """
        res = []
        ss = list(ss)
        if ss!=None and len(ss)>0:
            self.PermutationHelp(ss,0,res)
        return sorted(res)
    def PermutationHelp(self,ss,s,res):

        if s==len(ss)-1:
            if ''.join(ss) not in res:
                res.append(''.join(ss))
        else:
            for j in range(s,len(ss)):
                ss[s],ss[j] = ss[j],ss[s]
                print s,':swap before:',ss
                self.PermutationHelp(ss,s+1,res)
                ss[s],ss[j] =  ss[j],ss[s]

                print 'after swap',ss


        pass
    # def Permuta(self, begin,slist): 	
    # 	if len(slist)==1:
    # 		return begin + slist
    # 	tmp = []
    # 	for i in range(len(slist)):
    # 		tmp.append(begin + self.Permuta(,))
    # 	return tmp


s=Solution()

print s.Permutation('abcde')
print s.Permutation2('abcde')